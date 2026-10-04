# ChelseaHeat: Thermal Storage for Data Center Heat Reuse

NYU Sustainable Data Center Hackathon, Grundfos Waste Heat Reuse Challenge (Site 1: 111 8th Avenue).


**Live demo:** [hot-takes.streamlit.app](https://hot-takes.streamlit.app/)


We propose a phase change thermal battery at 111 8th Avenue that feeds data center heat into Con Edison's Chelsea thermal energy network, serving hot water to the rebuilt Fulton Houses on residents' schedule instead of the servers'. This repo is the decision tool behind that proposal: it tests the design hour by hour instead of relying on spreadsheet averages.

## What it does

1. **Hourly simulation (8,760 h)** of data center heat supply, NYCHA hot water demand, storage state of charge, outages and Con Ed steam backup (`heatsim/model.py`).
2. **Physics check on the storage.** The PCM can only charge or discharge when temperatures allow it. This revealed that an 84 F salt hydrate on the shared ambient loop (54 to 97 F) can barely charge in winter, so we moved it to the condenser water side.
3. **ML demand forecasting** (`heatsim/forecast.py`). A gradient-boosted model forecasts hourly demand a day ahead (about 8.5% MAPE, vs 9.0% for a simple hour-of-day profile and 17.5% for same-as-yesterday; with 40% space heating, 6.7% vs 22.5% for the profile). We use it to test outage reserve rules. At default settings no reserve beats all of them, because the battery is usually full when an outage starts (see results).
4. **Financial model** (`heatsim/finance.py`): capex, 30-year NPV, cost of heat, storage payback, customer bills, CO2 and water impact, plus sensitivities.
5. **Interactive app** (`app.py`) where every assumption is a slider.

## Run it

Use the [live demo](https://hot-takes.streamlit.app/), or run it locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Key results at default settings (synthetic data, see below)

| Metric | Value |
|---|---|
| Load served by data center heat | 99.9% (vs 95.5% with no storage) |
| Steam backup | about 10 MWh/yr (vs about 393 with no storage) |
| NYCHA hot water cost | about $32/MMBtu vs $40 for steam (about 20% saving) |
| CO2 avoided vs steam | about 1,370 t/yr |
| Cooling tower water saved | about 3.6M gal/yr (if towers are used) |
| Network cost of heat | about $46/MMBtu, needs utility cost recovery, rebuild trenching or commercial buyers |
| Water tank floor area vs PCM | about 7.8x on the loop side, about 3.5x on the condenser side (the fair comparison for our design) |
| Outage reserve rules (steam, MWh/yr) | no reserve 10, perfect foresight 20, ML forecast 33, hour-of-day profile 37, fixed 8 h worst case 185 |

Defaults: 1.5 MW capture, 1.0 MW average demand, 12 MWh PCM on the condenser side with 2.5 MW charge/discharge power (sized to peak demand, our assumption), no outage reserve.

**Honest findings:**
- With sublinear equipment costs and no floor-space credit, storage alone pays back in about 15 years, not the 4 to 8 years estimated in our earlier brief. The case for storage rests on reliability, floor space in a Manhattan cellar, and network growth, not on simple payback. Toggle the floor-space credit in the app to see the difference.
- Holding energy back for outages doesn't pay in this model. Capture (1.5 MW) exceeds average demand (1.0 MW), so the battery is usually full when an outage starts, and any reserve mostly blocks peak shaving. The fixed 8 h worst-case rule asks for 15.2 MWh, more than the battery holds.
- The space advantage over water is real but smaller than the brief's 8x once the store sits on the hotter condenser side, where a water tank can use a wider temperature swing.

## Data provenance (read this)

- **Demand and weather are synthetic**, calibrated to figures in our research brief (1.64 peak-to-average hot water ratio from Fulton data in the Con Ed Stage 2 filing; NYC temperature normals). No metered data for 111 8th Ave or the Fulton buildings is public.
- **To use real data:** replace `synth_weather` with `load_weather_csv` (NOAA Central Park hourly), and replace the training data in `forecast.py` with metered hot water data or NREL End-Use Load Profiles (ResStock) for New York multifamily buildings.
- Heat source size (1.5 MW) and condenser water temperature (90 F) are assumptions that must be confirmed by metering, as Con Ed did at 85 10th Avenue.
- All costs are planning estimates from cited benchmarks in `docs/`, not quotes.

## Team

3-person team, NYU Sustainable Data Center Hackathon 2026.

Built with help from [Claude Code](https://claude.com/claude-code) for the simulation, app and dashboard design.
