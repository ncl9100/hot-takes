# ChelseaHeat: Thermal Storage for Data Center Heat Reuse

NYU Sustainable Data Center Hackathon, Grundfos Waste Heat Reuse Challenge (Site 1: 111 8th Avenue).

We propose a phase change thermal battery at 111 8th Avenue that feeds data center heat into Con Edison's Chelsea thermal energy network, serving hot water to the rebuilt Fulton Houses on residents' schedule instead of the servers'. This repo is the decision tool behind that proposal: it tests the design hour by hour instead of relying on spreadsheet averages.

## What it does

1. **Hourly simulation (8,760 h)** of data center heat supply, NYCHA hot water demand, storage state of charge, outages and Con Ed steam backup (`heatsim/model.py`).
2. **Physics check on the storage.** The PCM can only charge or discharge when temperatures allow it. This revealed that an 84 F salt hydrate on the shared ambient loop (54 to 97 F) can barely charge in winter, so we moved it to the condenser water side.
3. **ML demand forecasting** (`heatsim/forecast.py`). A gradient-boosted model forecasts hourly demand a day ahead (about 8.5% MAPE vs 17.5% for a naive same-as-yesterday forecast). The forecast sets how much energy to hold in reserve for outages, so one battery can both shave daily peaks and provide ride-through instead of the capacity being counted twice.
4. **Financial model** (`heatsim/finance.py`): capex, 30-year NPV, cost of heat, storage payback, customer bills, CO2 and water impact, plus sensitivities.
5. **Interactive app** (`app.py`) where every assumption is a slider.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Key results at default settings (synthetic data, see below)

| Metric | Value |
|---|---|
| Load served by data center heat | 99.6% (vs 95.5% with no storage) |
| NYCHA hot water cost | about $32/MMBtu vs $40 for steam (about 20% saving) |
| CO2 avoided vs steam | about 1,370 t/yr |
| Cooling tower water saved | about 3.6M gal/yr (if towers are used) |
| Network cost of heat | about $46/MMBtu, needs utility cost recovery, rebuild trenching or commercial buyers |
| ML forecast vs fixed reserve | steam backup cut from about 190 to 37 MWh/yr |

**Honest finding:** with sublinear equipment costs and no floor-space credit, storage alone pays back in about 16 years, not the 4 to 8 years estimated in our earlier brief. The case for storage rests on reliability (8 h ride-through), floor space in a Manhattan cellar, and network growth, not on simple payback. Toggle the floor-space credit in the app to see the difference.

## Data provenance (read this)

- **Demand and weather are synthetic**, calibrated to figures in our research brief (1.64 peak-to-average hot water ratio from Fulton data in the Con Ed Stage 2 filing; NYC temperature normals). No metered data for 111 8th Ave or the Fulton buildings is public.
- **To use real data:** replace `synth_weather` with `load_weather_csv` (NOAA Central Park hourly), and replace the training data in `forecast.py` with metered hot water data or NREL End-Use Load Profiles (ResStock) for New York multifamily buildings.
- Heat source size (1.5 MW) and condenser water temperature (90 F) are assumptions that must be confirmed by metering, as Con Ed did at 85 10th Avenue.
- All costs are planning estimates from cited benchmarks in `docs/`, not quotes.

## Team

3-person team, NYU Sustainable Data Center Hackathon 2026.
