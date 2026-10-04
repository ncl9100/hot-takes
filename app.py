"""Interactive judge demo: streamlit run app.py"""
import numpy as np
import pandas as pd
import streamlit as st
from heatsim.model import (synth_weather, synth_demand, outage_mask, Storage, simulate, summarize)
from heatsim.forecast import train_and_forecast, reserve_policies
from heatsim import finance as fin

st.set_page_config(page_title="ChelseaHeat: Data Center Heat to NYCHA", layout="wide")
st.title("ChelseaHeat: thermal storage for data center heat reuse")
st.caption("111 8th Ave data center heat to the Fulton Houses rebuild via Con Ed's Chelsea thermal loop. "
           "Hourly simulation, ML demand forecasting and a financial model. "
           "Demand and weather are SYNTHETIC profiles calibrated to the brief's figures; see README for data provenance.")

with st.sidebar:
    st.header("System")
    capture = st.slider("Heat capture capacity (MW)", 0.5, 3.0, 1.5, 0.1)
    avg = st.slider("Average heat demand, source side (MW)", 0.3, 2.0, 1.0, 0.1)
    sh = st.slider("Space heating share of load", 0.0, 0.6, 0.0, 0.05,
                   help="0 = hot water only, the brief's anchor load")
    kind = st.selectbox("Storage technology", ["pcm", "water", "none"],
                        format_func={"pcm": "Phase change (salt hydrate)", "water": "Water tank", "none": "No storage"}.get)
    cap_mwh = st.slider("Storage capacity (MWh)", 0.0, 24.0, 12.0, 1.0)
    placement = st.radio("PCM placement", ["condenser", "loop"],
                         format_func={"condenser": "Hot side: condenser water (revised)",
                                      "loop": "Shared ambient loop (original brief)"}.get)
    melt = st.slider("PCM melt point (F)", 70, 95, 84)
    outage_h = st.slider("Data center heat outages (h/yr)", 0, 600, 200, 20)
    reserve_name = st.selectbox("Outage reserve policy", list(reserve_policies(pd.Series([1.0]), np.array([1.0])).keys()), index=1)
    ride = st.slider("Ride-through target (h)", 2, 12, 8)
    st.header("Economics")
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


@st.cache_data
def base_data(avg, sh, outage_h):
    w = synth_weather(seed=0)
    d = synth_demand(w, avg_source_mw=avg, space_heat_share=sh)
    o = outage_mask(d.index, hours=outage_h)
    pred, metrics = train_and_forecast(d, w, avg_source_mw=avg, space_heat_share=sh)
    return w, d, o, pred, metrics


w, d, o, pred, metrics = base_data(avg, sh, outage_h)
store = Storage(kind=kind, capacity_mwh=cap_mwh if kind != "none" else 0.0, power_mw=max(capture, 0.1),
                melt_f=melt, placement=placement)
policies = reserve_policies(d, pred.values, ride_through_h=ride)
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
c1.metric("Load served by data center heat", f"{s['network_share']:.1%}")
c2.metric("Steam backup needed", f"{s['steam_mwh']:,.0f} MWh/yr", f"{s['steam_mwh'] - s_none['steam_mwh']:,.0f} vs no storage", delta_color="inverse")
c3.metric("NYCHA hot water cost", f"${cust['total']:.0f}/MMBtu", f"{-cust['savings_pct']:.0%} vs steam", delta_color="inverse")
c4.metric("CO2 avoided vs steam", f"{imp['tco2_avoided_vs_steam']:,.0f} t/yr")
c5.metric("Network cost of heat", f"${net['lcoh']:.0f}/MMBtu", f"price ${net['avg_price']:.0f}", delta_color="off")

tabs = st.tabs(["Hourly operation", "Storage comparison", "ML forecast + reserve", "Financial model", "Assumptions"])

with tabs[0]:
    week = st.select_slider("Week of year", options=list(range(1, 53)), value=4)
    sl = res.iloc[(week - 1) * 168: week * 168]
    st.subheader("Heat balance (MW, source side)")
    st.line_chart(sl[["demand", "dc_supply", "discharge", "steam"]].rename(columns={
        "demand": "Demand", "dc_supply": "Data center supply", "discharge": "Storage discharge", "steam": "Steam backup"}))
    st.subheader("Storage state of charge (MWh)")
    st.area_chart(sl[["soc_mwh"]])
    if sl["outage"].any():
        st.info(f"This week includes {int(sl['outage'].sum())} hours of data center heat outage.")
    st.subheader("Monthly energy (MWh)")
    m = res.resample("MS")[["dc_direct", "discharge", "steam", "to_towers"]].sum()
    m.index = m.index.strftime("%b")
    st.bar_chart(m.rename(columns={"dc_direct": "DC heat direct", "discharge": "From storage",
                                   "steam": "Steam backup", "to_towers": "Rejected to towers"}), sort=False)

with tabs[1]:
    rows = []
    configs = {"No storage": Storage(kind="none", capacity_mwh=0),
               "Water tank": Storage(kind="water", capacity_mwh=cap_mwh, power_mw=capture),
               "PCM on shared loop (original)": Storage(capacity_mwh=cap_mwh, power_mw=capture, melt_f=melt, placement="loop"),
               "PCM on condenser water (revised)": Storage(capacity_mwh=cap_mwh, power_mw=capture, melt_f=melt, placement="condenser")}
    for name, cfg in configs.items():
        r = summarize(simulate(d, o, capture, cfg, policies[reserve_name]))
        rows.append({"Option": name, "Steam backup (MWh/yr)": round(r["steam_mwh"]),
                     "Hours on steam": r["steam_hours"], "Served by DC heat": f"{r['network_share']:.1%}",
                     "Volume (m3)": round(cfg.volume_m3()), "Floor area (sq ft)": round(cfg.footprint_sqft())})
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    st.markdown("**Finding:** on the shared loop, an 84 F PCM can only charge when the loop runs above ~87 F, "
                "which happens in summer, when heat is least needed. Moving it to the condenser water side "
                "(~90 F, ASSUMPTION to verify by metering) restores winter operation. A water tank performs the same "
                "but needs roughly 8x the floor area on this narrow-temperature loop.")
    sv = fin.storage_value(s, s_none, float(np.percentile(d, 99)), capture, store, configs["Water tank"], f)
    a, b, c, e = st.columns(4)
    a.metric("Storage net capex (after ITC)", f"${sv['storage_capex_net']/1e6:.2f}M")
    b.metric("Avoided capture capex", f"${sv['avoided_capture_capex']/1e6:.2f}M")
    c.metric("Annual savings", f"${(sv['annual_steam_savings'] + sv['annual_floor_value'])/1e3:,.0f}K")
    e.metric("Storage payback", "n/a" if not np.isfinite(sv["payback_years"]) else f"{sv['payback_years']:.1f} yr")

with tabs[2]:
    st.markdown("A gradient-boosted model forecasts hourly heat demand a day ahead from calendar features, "
                "temperature and lagged demand. The forecast sets **how much energy to hold back for outages**, "
                "so the same battery can also shave daily peaks.")
    a, b, c = st.columns(3)
    a.metric("ML forecast error (MAPE)", f"{metrics['ml_mape']:.1%}")
    b.metric("Naive 'same as yesterday' error", f"{metrics['persistence_mape']:.1%}")
    c.metric("Mean absolute error", f"{metrics['ml_mae_mw']*1000:.0f} kW")
    sl = slice((week - 1) * 168, week * 168)
    st.line_chart(pd.DataFrame({"Actual": d.iloc[sl], "ML forecast": pred.iloc[sl]}))
    rows = []
    for name, r in policies.items():
        x = summarize(simulate(d, o, capture, store, r))
        rows.append({"Reserve policy": name, "Steam, normal ops (MWh)": round(x["steam_mwh_normal_ops"], 1),
                     "Steam, during outages (MWh)": round(x["steam_mwh_during_outages"], 1),
                     "Total steam (MWh)": round(x["steam_mwh"], 1)})
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    st.caption("Model is trained on synthetic years calibrated to the brief. Replace with metered Fulton hot water "
               "data and NOAA weather before any real decision.")

with tabs[3]:
    a, b, c, e = st.columns(4)
    a.metric("Total capex (gross)", f"${net['capex_gross']/1e6:.1f}M")
    b.metric("Net to network owner", f"${net['capex_net_to_owner']/1e6:.1f}M")
    c.metric("NPV (30 yr, 6%)", f"${net['npv']/1e6:.1f}M")
    e.metric("Payback", "beyond 30 yr" if net["payback_years"] is None else f"{net['payback_years']} yr")
    st.subheader("Capital cost breakdown")
    st.bar_chart(pd.Series(net["capex_lines"]) / 1e6)
    st.subheader("Cumulative cash flow ($M)")
    st.line_chart(pd.Series(np.cumsum(net["cashflow"]) / 1e6, name="Cumulative cash flow"))
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
    st.metric("Water saved at cooling towers", f"{imp['water_gal_saved']/1e6:.1f}M gal/yr")

with tabs[4]:
    st.markdown("""
- **Heat source:** 1.5 MW captured from one tenant's condenser loop at 111 8th Ave. ASSUMPTION; the building's cooling plant data is not public. Must be metered.
- **Demand:** synthetic hourly hot water profile with the brief's 1.64 peak-to-average ratio, seasonal inlet temperature effect and random variation. Not metered data.
- **Loop temperatures:** 54 to 97 F seasonal range and 10 F supply/return swing from the Con Ed Stage 2 filing; seasonal shape is our assumption. Condenser water at 90 F is our assumption.
- **Storage:** salt hydrate (CaCl2.6H2O, ~84 F melt, ~50 kWh/m3 system density), 86% round trip, 1%/day standby loss.
- **Costs:** capture $2.5M per 1.5 MW scaled with exponent 0.6; storage $120/kWh; pipe $6,000/ft x 1,200 ft; 25% soft costs; 30% ITC on storage; 6% over 30 years; O&M 2%/yr.
- **Carbon:** NYC Local Law 97 2030 coefficients. **Water:** ~8,300 Btu per gallon evaporated, only if the plant uses cooling towers.
""")
