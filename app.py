"""Interactive judge demo: streamlit run app.py"""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from heatsim.model import (synth_weather, synth_demand, outage_mask, Storage, simulate, summarize)
from heatsim.forecast import train_and_forecast, reserve_policies, POLICY_NAMES
from heatsim import finance as fin

st.set_page_config(page_title="ChelseaHeat: Data Center Heat to NYCHA", layout="wide")
st.markdown("""
<style>
  .block-container {padding-top: 3.6rem;}
  .ch-head {display: flex; align-items: center; gap: .6rem; flex-wrap: wrap; margin-bottom: .1rem;}
  .ch-head h1 {font-size: 1.6rem; margin: 0; padding: 0; line-height: 1.2;}
  .ch-badge {font-size: .72rem; font-weight: 600; letter-spacing: .02em; padding: .12rem .5rem; border-radius: 999px;
             background: #fff4e5; color: #9a4b00; border: 1px solid #f5c98b; white-space: nowrap;}
  .ch-sub {color: #5b6472; font-size: .92rem; margin: 0 0 .6rem 0;}
  [data-testid="stMetric"] {min-height: 6.4rem;}
  [data-testid="stMetricLabel"] p {white-space: normal; overflow: visible; text-overflow: clip;}
  [data-testid="stMetricValue"] div {overflow: visible; text-overflow: clip;}
</style>
<div class="ch-head"><h1>ChelseaHeat</h1>
  <span class="ch-badge" title="Demand and weather are synthetic profiles calibrated to the brief's figures; see README">SYNTHETIC DATA</span></div>
<p class="ch-sub">Data center heat from 111 8th Ave, stored in a phase change battery, delivered to the Fulton Houses rebuild via Con Ed's Chelsea loop.</p>
""", unsafe_allow_html=True)

with st.sidebar:
    with st.expander("System", expanded=True):
        capture = st.slider("Heat capture capacity (MW)", 0.5, 3.0, 1.5, 0.1)
        avg = st.slider("Average heat demand, source side (MW)", 0.3, 2.0, 1.0, 0.1)
        sh = st.slider("Space heating share of load", 0.0, 0.6, 0.0, 0.05,
                       help="0 = hot water only, the brief's anchor load")
    with st.expander("Storage", expanded=True):
        kind = st.selectbox("Storage technology", ["pcm", "water", "none"],
                            format_func={"pcm": "Phase change (salt hydrate)", "water": "Water tank", "none": "No storage"}.get)
        cap_mwh = st.slider("Storage capacity (MWh)", 0.0, 24.0, 12.0, 1.0)
        store_mw = st.slider("Storage charge/discharge power (MW)", 0.5, 4.0, 2.5, 0.1,
                             help="ASSUMPTION: sized to peak demand (~2.4 MW at defaults), not to capture")
        placement = st.radio("PCM placement", ["condenser", "loop"],
                             format_func={"condenser": "Hot side: condenser water (revised)",
                                          "loop": "Shared ambient loop (original brief)"}.get)
        melt = st.slider("PCM melt point (F)", 70, 95, 84)
    with st.expander("Operations"):
        outage_h = st.slider("Data center heat outages (h/yr)", 0, 600, 200, 20)
        reserve_name = st.selectbox("Outage reserve policy", POLICY_NAMES, index=POLICY_NAMES.index("No reserve"),
                                    help="No reserve gives the least steam in this model; see the ML tab")
        ride = st.slider("Ride-through target (h)", 2, 12, 8)
    with st.expander("Economics"):
        heat_price = st.slider("NYCHA heat price ($/MMBtu source heat)", 5.0, 50.0, 15.0, 1.0)
        com_share = st.slider("Share sold to commercial (LL97) buyers", 0.0, 0.6, 0.0, 0.05)
        com_price = st.slider("Commercial price ($/MMBtu)", 15.0, 60.0, 35.0, 1.0)
        pcm_cost = st.slider("Installed storage cost ($/kWh)", 40, 200, 120, 5)
        pipe_cost = st.slider("Pipe cost ($/ft)", 1000, 10000, 6000, 500,
                              help="~$2,000 if laid during rebuild site work")
        ratepayer = st.slider("Capex recovered via utility rates", 0.0, 1.0, 0.0, 0.05)
        elec = st.slider("Electricity price ($/kWh)", 0.10, 0.40, 0.25, 0.01)
        steam = st.slider("Con Ed steam price ($/MMBtu)", 20.0, 60.0, 40.0, 1.0)
        floor = st.checkbox("Credit floor space saved vs a water tank", False)


# One color per meaning, shared by every chart: blue = data center heat, orange = storage,
# gray = steam backup, light red = rejected to towers. Other series get neutral, non-clashing hues.
DC, STORE, STEAM, TOWERS = "#2b6cb0", "#e8871e", "#8a9099", "#f08c8c"
COLORS = {"Data center supply": DC, "DC heat direct": DC, "Storage discharge": STORE, "From storage": STORE,
          "State of charge": STORE, "Steam backup": STEAM, "Rejected to towers": TOWERS,
          "Demand": "#1f2937", "Actual": "#1f2937", "ML forecast": "#0f766e", "Profile (no ML)": "#9b6bcc",
          "Capital cost": "#0f766e", "Cumulative cash flow": "#0f766e"}
DASHED = {"Demand", "Profile (no ML)"}


def chart(df, kind="line", y_title="", x_title=None, height=300, caption=None):
    """Altair chart with hover tooltips but no scroll-zoom or pan. A text x axis keeps df's row order.
    Series colors come from COLORS; every chart gets a legend and an optional one-line caption."""
    df = df.to_frame() if isinstance(df, pd.Series) else df
    series = list(df.columns)
    data = df.rename_axis("x").reset_index().melt("x", var_name="Series", value_name="value")
    data["order"] = data["Series"].map({c: i for i, c in enumerate(series)})  # bars stack in column order
    if isinstance(df.index, pd.DatetimeIndex):
        x, x_tip = alt.X("x:T", title=x_title), alt.Tooltip("x:T", title="Time", format="%b %d %H:00")
    elif pd.api.types.is_numeric_dtype(df.index):
        x, x_tip = alt.X("x:Q", title=x_title), alt.Tooltip("x:Q", title=x_title or "x")
    else:
        x, x_tip = alt.X("x:N", sort=None, title=x_title, axis=alt.Axis(labelAngle=0, labelLimit=0)), alt.Tooltip("x:N", title=x_title or " ")
    mark = {"line": alt.Chart(data).mark_line(strokeWidth=2.2), "area": alt.Chart(data).mark_area(opacity=0.45, line=True),
            "bar": alt.Chart(data).mark_bar()}[kind]
    enc = {"x": x, "y": alt.Y("value:Q", title=y_title),
           "tooltip": [x_tip, alt.Tooltip("Series:N"), alt.Tooltip("value:Q", title=y_title or "Value", format=",.2f")],
           "color": alt.Color("Series:N", title=None, sort=series,
                              scale=alt.Scale(domain=series, range=[COLORS.get(c, "#0f766e") for c in series]),
                              legend=alt.Legend(orient="bottom", labelFontSize=12, symbolStrokeWidth=3))}
    if kind == "line":
        enc["strokeDash"] = alt.StrokeDash("Series:N", sort=series, legend=None, scale=alt.Scale(
            domain=series, range=[[6, 3] if c in DASHED else [1, 0] for c in series]))
    if kind == "bar":
        enc["order"] = alt.Order("order:Q")
    st.altair_chart(mark.encode(**enc).properties(height=height)
                    .configure_axis(labelFontSize=12, titleFontSize=12, gridColor="#eceff3"),
                    width="stretch")
    if caption:
        st.caption(f"**What this shows:** {caption}")


@st.cache_data
def base_data(avg, sh, outage_h):
    w = synth_weather(seed=0)
    d = synth_demand(w, avg_source_mw=avg, space_heat_share=sh)
    o = outage_mask(d.index, hours=outage_h)
    pred, profile, metrics = train_and_forecast(d, w, avg_source_mw=avg, space_heat_share=sh)
    return w, d, o, pred, profile, metrics


w, d, o, pred, profile, metrics = base_data(avg, sh, outage_h)
store = Storage(kind=kind, capacity_mwh=cap_mwh if kind != "none" else 0.0, power_mw=store_mw,
                melt_f=melt, placement=placement)
policies = reserve_policies(d, pred.values, profile.values, ride_through_h=ride)
res = simulate(d, o, capture, store, policies[reserve_name])
s = summarize(res)
s_none = summarize(simulate(d, o, capture, Storage(kind="none")))
f = fin.FinanceInputs(storage_cost_per_kwh=pcm_cost, pipe_cost_per_ft=pipe_cost, heat_price=heat_price,
                      commercial_share=com_share, commercial_price=com_price, ratepayer_share=ratepayer,
                      elec_price=elec, steam_price=steam, count_floor_space=floor)
net = fin.network(s, capture, store.capacity_mwh, f)
cust = fin.customer(f)
imp = fin.impact(s, f)

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("DC heat share", f"{s['network_share']:.1%}", border=True,
          help="Share of hot water load served by data center heat (directly or via storage)")
c2.metric("Steam backup", f"{s['steam_mwh']:,.0f} MWh/yr", f"{s['steam_mwh'] - s_none['steam_mwh']:,.0f} vs no storage",
          delta_color="inverse", border=True, help="Con Ed steam needed to cover the rest of the load")
c3.metric("NYCHA cost", f"${cust['total']:.0f}/MMBtu", f"{-cust['savings_pct']:.0%} vs steam", delta_color="inverse",
          border=True, help="NYCHA hot water cost: heat pump electricity plus network heat charge")
c4.metric("CO2 avoided", f"{imp['tco2_avoided_vs_steam']:,.0f} t/yr", border=True,
          help="Tonnes CO2 avoided vs Con Ed steam, Local Law 97 2030 coefficients")
c5.metric("Cost of heat", f"${net['lcoh']:.0f}/MMBtu", f"price ${net['avg_price']:.0f}", delta_color="off",
          border=True, help="Network levelized cost of heat vs the average sale price")

tabs = st.tabs(["Hourly operation", "Storage comparison", "ML forecast + reserve", "Financial model", "Assumptions"])

with tabs[0]:
    week = st.select_slider("Week of year", options=list(range(1, 53)), value=4)
    sl = res.iloc[(week - 1) * 168: week * 168]
    st.subheader("Heat balance (MW, source side)")
    chart(sl[["demand", "dc_supply", "discharge", "steam"]].rename(columns={
        "demand": "Demand", "dc_supply": "Data center supply", "discharge": "Storage discharge", "steam": "Steam backup"}),
        y_title="MW", caption="Hour by hour for the selected week: the dashed line is hot water demand, blue is the "
        "heat the data center can supply, and orange and gray show storage and steam filling any gap.")
    st.subheader("Storage state of charge (MWh)")
    chart(sl["soc_mwh"].rename("State of charge"), kind="area", y_title="MWh",
          caption="How full the thermal battery is: it charges when data center heat exceeds demand and drains "
          "at demand peaks and during outages.")
    if sl["outage"].any():
        st.info(f"This week includes {int(sl['outage'].sum())} hours of data center heat outage.")
    st.subheader("Monthly energy (MWh)")
    m = res.resample("MS")[["dc_direct", "discharge", "steam", "to_towers"]].sum()
    m.index = m.index.strftime("%b")
    chart(m.rename(columns={"dc_direct": "DC heat direct", "discharge": "From storage",
                            "steam": "Steam backup", "to_towers": "Rejected to towers"}), kind="bar", y_title="MWh",
          caption="Where each month's heat comes from, plus surplus data center heat still sent to the cooling "
          "towers; the steam slice is too thin to see when storage covers nearly every gap (hover for values).")

with tabs[1]:
    rows = []
    tank_loop = Storage(kind="water", capacity_mwh=cap_mwh, power_mw=store_mw, placement="loop")
    tank_cond = Storage(kind="water", capacity_mwh=cap_mwh, power_mw=store_mw, placement="condenser")
    configs = {"No storage": Storage(kind="none", capacity_mwh=0),
               f"Water tank, loop side ({tank_loop.water_swing_c():.1f} C swing)": tank_loop,
               f"Water tank, condenser side ({tank_cond.water_swing_c():.1f} C swing)": tank_cond,
               "PCM on shared loop (original)": Storage(capacity_mwh=cap_mwh, power_mw=store_mw, melt_f=melt, placement="loop"),
               "PCM on condenser water (revised)": Storage(capacity_mwh=cap_mwh, power_mw=store_mw, melt_f=melt, placement="condenser")}
    for name, cfg in configs.items():
        r = summarize(simulate(d, o, capture, cfg, policies[reserve_name]))
        rows.append({"Option": name, "Steam backup (MWh/yr)": round(r["steam_mwh"]),
                     "Hours on steam": r["steam_hours"], "Served by DC heat": f"{r['network_share']:.1%}",
                     "Volume (m3)": round(cfg.volume_m3()), "Floor area (sq ft)": round(cfg.footprint_sqft())})
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    ratio = (lambda t: Storage().pcm_kwh_per_m3 / t.water_kwh_per_m3())  # floor area ratio = density ratio
    st.markdown("**Finding:** on the shared loop, an 84 F PCM can only charge when the loop runs above ~87 F, "
                "which happens in summer, when heat is least needed. Moving it to the condenser water side "
                "(~90 F, ASSUMPTION to verify by metering) restores winter operation. A water tank stores the same "
                f"energy but needs about {ratio(tank_loop):.1f}x the PCM's floor area on the loop side and about "
                f"{ratio(tank_cond):.1f}x on the condenser side, where it can swing from 87 F down to 65 F "
                "(ASSUMPTION). The fair comparison for the revised design is the condenser-side tank.")
    sv = fin.storage_value(s, s_none, float(np.percentile(d, 99)), capture, store,
                           tank_loop if placement == "loop" else tank_cond, f)
    a, b, c, e = st.columns(4)
    a.metric("Storage capex", f"${sv['storage_capex_net']/1e6:.2f}M", border=True, help="Storage net capex after the 30% ITC")
    b.metric("Capture avoided", f"${sv['avoided_capture_capex']/1e6:.2f}M", border=True,
             help="Heat capture capex avoided because storage covers peaks")
    c.metric("Annual savings", f"${(sv['annual_steam_savings'] + sv['annual_floor_value'])/1e3:,.0f}K", border=True,
             help="Avoided steam purchases, plus floor space value if credited")
    e.metric("Storage payback", "n/a" if not np.isfinite(sv["payback_years"]) else f"{sv['payback_years']:.1f} yr",
             border=True)

with tabs[2]:
    st.markdown("A gradient-boosted model forecasts hourly heat demand a day ahead from calendar features, "
                "temperature and lagged demand. We test whether a forecast-based **outage reserve** (energy held "
                "back for the next ride-through hours) cuts steam compared with simpler rules, including holding "
                "no reserve at all.")
    a, b, c, e = st.columns(4)
    a.metric("ML error (MAPE)", f"{metrics['ml_mape']:.1%}", border=True,
             help="Mean absolute percentage error of the gradient-boosted day-ahead forecast")
    b.metric("Profile error", f"{metrics['profile_mape']:.1%}", border=True,
             help="Hour-of-day average profile, no ML (MAPE)")
    c.metric("Naive error", f"{metrics['persistence_mape']:.1%}", border=True,
             help="Naive 'same as yesterday' forecast (MAPE)")
    e.metric("ML error (MAE)", f"{metrics['ml_mae_mw']*1000:.0f} kW", border=True, help="ML mean absolute error")
    sl = slice((week - 1) * 168, week * 168)
    st.subheader("Day-ahead demand forecast (MW, source side)")
    chart(pd.DataFrame({"Actual": d.iloc[sl], "ML forecast": pred.iloc[sl], "Profile (no ML)": profile.iloc[sl]}),
          y_title="MW", caption="Forecasts against actual (synthetic) demand for the week chosen on the first tab: "
          "the closer a line tracks the solid dark one, the better the forecast.")
    rows = []
    for name, r in policies.items():
        x = summarize(simulate(d, o, capture, store, r))
        rows.append({"Reserve policy": name, "Avg reserve held (MWh)": round(float(np.minimum(r, store.capacity_mwh).mean()), 1),
                     "Steam, normal ops (MWh)": round(x["steam_mwh_normal_ops"], 1),
                     "Steam, during outages (MWh)": round(x["steam_mwh_during_outages"], 1),
                     "Total steam (MWh)": round(x["steam_mwh"], 1)})
    pol = pd.DataFrame(rows)
    st.dataframe(pol, hide_index=True, width="stretch")
    best = pol.loc[pol["Total steam (MWh)"].idxmin(), "Reserve policy"]
    fixed = policies[POLICY_NAMES[0]][0]
    st.markdown(f"**Finding:** at these settings **{best}** gives the least steam. The fixed worst-case rule asks for "
                f"{fixed:.1f} MWh, {'more than' if fixed > store.capacity_mwh else 'up to'} the {store.capacity_mwh:.0f} MWh "
                "battery, so it blocks most peak shaving. At the default settings capture exceeds average demand, "
                "so the battery is usually full when an outage starts and holding a reserve costs more steam in "
                "normal hours than it saves during outages. On hot-water-only load the ML forecast is barely more accurate than the hour-of-day "
                "profile. With space heating the load becomes weather-driven and the ML forecast is far more accurate "
                "(try the slider), but a better forecast still does not turn into less steam while no reserve wins.")
    st.caption("SYNTHETIC: the model is trained and tested on synthetic years calibrated to the brief, so forecast "
               "errors mostly reflect the noise we injected. Replace with metered Fulton hot water data and NOAA "
               "weather before any real decision.")

with tabs[3]:
    a, b, c, e = st.columns(4)
    a.metric("Capex (gross)", f"${net['capex_gross']/1e6:.1f}M", border=True, help="Total capex, gross")
    b.metric("Net to owner", f"${net['capex_net_to_owner']/1e6:.1f}M", border=True,
             help="Capex net to the network owner after ITC and rate recovery")
    c.metric("NPV (30 yr, 6%)", f"${net['npv']/1e6:.1f}M", border=True)
    e.metric("Payback", "beyond 30 yr" if net["payback_years"] is None else f"{net['payback_years']} yr", border=True)
    st.subheader("Capital cost breakdown")
    chart(pd.Series(net["capex_lines"], name="Capital cost") / 1e6, kind="bar", y_title="$M",
          caption="What the system costs to build, by component, in millions of dollars before incentives.")
    st.subheader("Cumulative cash flow ($M)")
    chart(pd.Series(np.cumsum(net["cashflow"]) / 1e6, name="Cumulative cash flow"), y_title="$M", x_title="Year",
          caption="Running total of money spent and earned by the network owner over 30 years; payback would be where the line crosses zero.")
    st.subheader("Who pays, who gains (per MMBtu of hot water delivered)")
    st.dataframe(pd.DataFrame([
        {"Item": "Heat pump electricity", "$/MMBtu": round(cust["electricity"], 2)},
        {"Item": "Network heat charge", "$/MMBtu": round(cust["network_charge"], 2)},
        {"Item": "Total via network", "$/MMBtu": round(cust["total"], 2)},
        {"Item": "Con Ed steam today", "$/MMBtu": round(cust["steam"], 2)}]), hide_index=True)
    st.subheader("Sensitivity: cost of heat ($/MMBtu)")
    rows = []
    for label, kw in [("Pipe laid during rebuild ($2,000/ft)", {"pipe_cost_per_ft": 2000}),
                      ("PCM at $80/kWh", {"storage_cost_per_kwh": 80}),
                      ("PCM at $150/kWh", {"storage_cost_per_kwh": 150}),
                      ("50% utility cost recovery", {"ratepayer_share": 0.5})]:
        g = fin.FinanceInputs(**{**f.__dict__, **kw})
        rows.append({"Scenario": label, "Cost of heat": round(fin.network(s, capture, store.capacity_mwh, g)["lcoh"], 1)})
    rows.insert(0, {"Scenario": "Current settings", "Cost of heat": round(net["lcoh"], 1)})
    st.dataframe(pd.DataFrame(rows), hide_index=True)
    st.metric("Water saved at cooling towers", f"{imp['water_gal_saved']/1e6:.1f}M gal/yr", border=True)

with tabs[4]:
    st.markdown("""
- **Heat source:** 1.5 MW captured from one tenant's condenser loop at 111 8th Ave. ASSUMPTION; the building's cooling plant data is not public. Must be metered.
- **Demand:** synthetic hourly hot water profile with the brief's 1.64 peak-to-average ratio, seasonal inlet temperature effect and random variation. Not metered data.
- **Loop temperatures:** 54 to 97 F seasonal range and 10 F supply/return swing from the Con Ed Stage 2 filing; seasonal shape is our assumption. Condenser water at 90 F is our assumption.
- **Storage:** salt hydrate (CaCl2.6H2O, ~84 F melt, ~50 kWh/m3 system density), 86% round trip, 1%/day standby loss. Charge/discharge power 2.5 MW by default, sized to peak demand (ASSUMPTION). Water tank comparison: 5.6 C swing on the loop side (brief), 87 to 65 F swing on the condenser side (ASSUMPTION).
- **Costs:** capture $2.5M per 1.5 MW scaled with exponent 0.6; storage $120/kWh; pipe $6,000/ft x 1,200 ft; 25% soft costs; 30% ITC on storage; 6% over 30 years; O&M 2%/yr.
- **Carbon:** NYC Local Law 97 2030 coefficients. **Water:** ~8,300 Btu per gallon evaporated, only if the plant uses cooling towers.
""")
