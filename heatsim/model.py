"""Hourly simulation of data center heat -> thermal storage -> NYCHA hot water.

Site: 111 8th Ave (heat source) to the Fulton campus via Con Ed's Chelsea loop.
Defaults trace to the team research brief in docs/. Anything marked ASSUMPTION
is ours and should be stated as such in the presentation.
All power values are SOURCE-SIDE heat (MW thermal taken from the data center).
"""
from dataclasses import dataclass
import numpy as np
import pandas as pd

HOURS = 8760
MMBTU_PER_MWH = 3.41214


# ---------------------------------------------------------------- weather
def synth_weather(seed=0, year=2025):
    """Synthetic NYC-like hourly air temperature (deg C).
    ASSUMPTION: seasonal + diurnal sinusoids + AR(1) noise, tuned to NYC normals.
    Replace with NOAA Central Park hourly data via load_weather_csv()."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range(f"{year}-01-01", periods=HOURS, freq="h")
    doy = np.arange(HOURS) // 24
    hod = np.arange(HOURS) % 24
    base = 12.9 - 11.5 * np.cos(2 * np.pi * (doy - 20) / 365) + 4.0 * np.sin(2 * np.pi * (hod - 9) / 24)
    noise = np.zeros(HOURS)
    e = rng.normal(0, 0.6, HOURS)
    for i in range(1, HOURS):
        noise[i] = 0.97 * noise[i - 1] + e[i]
    return pd.DataFrame({"temp_c": base + noise}, index=idx)


def load_weather_csv(path):
    """Real data hook: CSV with columns timestamp,temp_c (hourly, one year)."""
    df = pd.read_csv(path, parse_dates=["timestamp"]).set_index("timestamp")
    return df[["temp_c"]].iloc[:HOURS]


# ---------------------------------------------------------------- demand
# Typical multifamily hot water draw by hour (relative). Morning + evening peaks.
_RAW = np.array([0.45, 0.35, 0.30, 0.30, 0.40, 0.70, 1.30, 1.75, 1.60, 1.30, 1.10, 1.00,
                 0.95, 0.90, 0.85, 0.90, 1.05, 1.35, 1.60, 1.55, 1.40, 1.20, 0.90, 0.65])


def dhw_shape(peak_ratio=1.64):
    """Daily shape with mean 1 and max = peak_ratio (brief: 1.64x from Fulton data)."""
    r = _RAW / _RAW.mean()
    dev = r - 1
    return 1 + dev * (peak_ratio - 1) / dev.max()


def synth_demand(weather, avg_source_mw=1.0, peak_ratio=1.64, space_heat_share=0.0, seed=1):
    """Source-side heat demand (MW) for the connected NYCHA buildings.
    Hot water scales with cold-water inlet temperature (higher in winter).
    space_heat_share: fraction of annual load that is space heating (0 = hot water only,
    which is the brief's anchor load)."""
    rng = np.random.default_rng(seed)
    idx = weather.index
    hod = idx.hour.values
    weekend = idx.dayofweek.values >= 5
    wd = dhw_shape(peak_ratio)
    we = np.roll(wd, 2) * 1.05  # weekends: later, slightly larger peak (ASSUMPTION)
    shape = np.where(weekend, we[hod], wd[hod])
    t_month = weather["temp_c"].rolling(24 * 30, min_periods=1).mean().values
    t_inlet = 12.5 + 0.6 * (t_month - 12.9)          # ASSUMPTION: mains water lags air temp
    seasonal = (60 - t_inlet) / (60 - 12.5)
    daily = np.repeat(rng.normal(1, 0.05, HOURS // 24 + 1), 24)[:HOURS]
    hourly = np.exp(rng.normal(0, 0.08, HOURS))
    dhw = shape * seasonal * daily * hourly
    dhw = dhw / dhw.mean()
    load = dhw
    if space_heat_share > 0:
        hdh = np.clip(18 - weather["temp_c"].values, 0, None) * shape ** 0.3
        load = (1 - space_heat_share) * dhw + space_heat_share * hdh / hdh.mean()
    return pd.Series(load * avg_source_mw, index=idx, name="demand_mw")


def outage_mask(index, hours=200, event_len=8, seed=2):
    """Data center heat interruptions (maintenance, tenant changes). Brief: ~200 h/yr."""
    rng = np.random.default_rng(seed)
    m = np.zeros(len(index), bool)
    n = max(0, int(round(hours / event_len)))
    if n:
        for s in rng.choice(len(index) - event_len, n, replace=False):
            m[s:s + event_len] = True
    return m


# ---------------------------------------------------------------- storage
@dataclass
class Storage:
    kind: str = "pcm"              # none | water | pcm
    capacity_mwh: float = 12.0     # brief: 12 MWh = 8 h at 1.5 MW
    power_mw: float = 1.5
    round_trip: float = 0.86       # brief: 80-92% daily cycles
    standby_loss_per_day: float = 0.01   # ASSUMPTION
    melt_f: float = 84.0           # CaCl2.6H2O ~29 C
    approach_f: float = 3.0        # ASSUMPTION: min temperature difference for heat transfer
    placement: str = "condenser"   # condenser (hot side, our fix) | loop (as in original brief)
    pcm_kwh_per_m3: float = 50.0   # brief: 12 MWh in 240 m3
    water_kwh_per_m3: float = 6.5  # brief: 1.16 kWh/m3/C x 5.6 C swing
    height_m: float = 3.05

    def volume_m3(self):
        if self.kind == "none":
            return 0.0
        d = self.pcm_kwh_per_m3 if self.kind == "pcm" else self.water_kwh_per_m3
        return self.capacity_mwh * 1000 / d

    def footprint_sqft(self):
        return self.volume_m3() / self.height_m * 10.764


def loop_supply_f(index):
    """Shared ambient loop supply temp. Brief: 54-97 F across the year.
    ASSUMPTION: seasonal sinusoid between those bounds, coldest late January."""
    doy = index.dayofyear.values - 1
    return 75.5 - 21.5 * np.cos(2 * np.pi * (doy - 20) / 365)


CONDENSER_F = 90.0  # ASSUMPTION: typical condenser water leaving chillers; verify by metering


def temperature_windows(index, st, outage):
    """When can the store physically charge / discharge? This is the check that
    exposes the melt-point problem in the original design."""
    n = len(index)
    if st.kind == "none" or st.capacity_mwh <= 0:
        return np.zeros(n, bool), np.zeros(n, bool)
    if st.kind == "water":
        return np.ones(n, bool), np.ones(n, bool)
    t_loop = loop_supply_f(index)
    t_src = t_loop if st.placement == "loop" else np.full(n, CONDENSER_F)
    charge_ok = t_src >= st.melt_f + st.approach_f
    t_return = t_loop - 10  # brief: max 10 F supply/return swing
    discharge_ok = (t_return <= st.melt_f - st.approach_f) | outage
    return charge_ok, discharge_ok


def simulate(demand, outage, capture_mw, st, reserve_mwh=None):
    """Hourly dispatch. Data center heat serves demand first, surplus charges the store,
    deficits draw from the store (down to a reserve floor except during outages),
    and anything left is covered by Con Ed steam backup."""
    D = demand.values
    n = len(D)
    S = np.where(outage, 0.0, capture_mw)
    cap = st.capacity_mwh if st.kind != "none" else 0.0
    eta = np.sqrt(st.round_trip)
    keep = (1 - st.standby_loss_per_day) ** (1 / 24)
    ch_ok, dis_ok = temperature_windows(demand.index, st, outage)
    res = np.zeros(n) if reserve_mwh is None else np.minimum(np.asarray(reserve_mwh, float), cap)
    soc = cap  # start full
    out = np.zeros((n, 6))
    for t in range(n):
        direct = min(S[t], D[t])
        surplus, deficit = S[t] - direct, D[t] - direct
        ch = dis = 0.0
        if surplus > 0 and ch_ok[t] and cap > 0:
            ch = min(surplus, st.power_mw, (cap - soc) / eta)
            soc += ch * eta
        if deficit > 0 and dis_ok[t] and cap > 0:
            floor = 0.0 if outage[t] else res[t]
            dis = min(deficit, st.power_mw, max(0.0, soc - floor) * eta)
            soc -= dis / eta
        steam = deficit - dis
        soc *= keep
        out[t] = (direct, ch, dis, steam, soc, surplus - ch)
    df = pd.DataFrame(out, index=demand.index,
                      columns=["dc_direct", "charge", "discharge", "steam", "soc_mwh", "to_towers"])
    df["demand"] = D
    df["dc_supply"] = S
    df["outage"] = outage
    return df


def summarize(df):
    steam = df["steam"]
    served = df["demand"].sum() - steam.sum()
    return {
        "demand_mwh": df["demand"].sum(),
        "served_by_network_mwh": served,
        "network_share": served / df["demand"].sum(),
        "steam_mwh": steam.sum(),
        "steam_hours": int((steam > 1e-6).sum()),
        "steam_mwh_during_outages": steam[df["outage"]].sum(),
        "steam_mwh_normal_ops": steam[~df["outage"]].sum(),
        "peak_steam_mw": steam.max(),
        "storage_cycles": df["discharge"].sum() / max(df["soc_mwh"].max(), 1e-9),
    }
