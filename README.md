# ChelseaHeat: Thermal Storage for Data Center Heat Reuse

NYU Sustainable Data Center Hackathon, Grundfos Waste Heat Reuse Challenge (Site 1: 111 8th Avenue).

**Live demo:** [hot-takes.streamlit.app](https://hot-takes.streamlit.app/)

**The problem:** a data center makes heat around the clock and sends most of it to rooftop cooling towers, while apartment buildings need hot water in morning and evening peaks. Steady supply and peaky demand don't line up, so heat is thrown away at night and Con Ed steam covers the peaks.

**Our answer:** a phase change thermal battery (salt hydrate, about 84 F melt point) at 111 8th Avenue that stores data center heat and feeds it into Con Edison's Chelsea thermal energy network, serving hot water to the rebuilt Fulton Houses on residents' schedule instead of the servers'.

**This repo** is the decision tool behind that proposal. It tests the design hour by hour instead of relying on spreadsheet averages. On the live dashboard you can change the inputs, or ask an AI assistant that answers by running the same model.

## What it does

1. **Hourly simulation (8,760 h)** of data center heat supply, NYCHA hot water demand, storage state of charge, outages and Con Ed steam backup (`heatsim/model.py`). See [How dispatch works](#how-dispatch-works).
2. **Physics check on the storage.** The PCM can only charge or discharge when temperatures allow it. This revealed that an 84 F salt hydrate on the shared ambient loop (54 to 97 F) can barely charge in winter, so we moved it to the condenser water side.
3. **ML demand forecasting** (`heatsim/forecast.py`). A gradient-boosted model forecasts hourly demand a day ahead and is used to test outage reserve rules. See [How the forecast connects to dispatch](#how-the-forecast-connects-to-dispatch).
4. **Financial model** (`heatsim/finance.py`): capex, 30-year NPV, cost of heat, storage payback, customer bills, CO2 and water impact, plus sensitivities.
5. **Interactive dashboard** (`app.py`) with five tabs (Hourly operation, Storage comparison, ML forecast + reserve, Financial model, Assumptions) and 20 sidebar inputs grouped into System, Storage, Operations and Economics. Some constants are not sliders: 86% round trip efficiency and 1%/day standby loss are listed on the Assumptions tab, and others, such as the heat pump COP of 3.4, are set in `heatsim/finance.py`.
6. **"Ask ChelseaHeat" AI assistant** (`assistant.py`), a chat button on every tab. Claude answers judges' questions by calling read-only tools that rerun the same pipeline as the dashboard:
   - `run_scenario`: KPIs for one set of inputs
   - `compare_scenarios`: 2 to 6 scenarios side by side
   - `get_assumptions`: assumption list, default values with sources, input ranges
   - `search_docs`: keyword search over the research files in `docs/`

   It starts from the current sidebar settings, shows the tool calls under each answer, and is instructed to take every number from a tool result or a `docs/` passage. Limits: 15 answered questions per session, 500 characters per question, up to 5 tool calls per answer.
7. **Intro screen** (`intro.py`): a short animation of the heat chain covers the first cold load (library imports and ML training). It is skipped once results are cached.

## How dispatch works

Each hour, `simulate()` in `heatsim/model.py` applies four rules in order:

1. Data center heat serves demand directly.
2. Surplus heat charges the storage, if temperatures allow charging, up to the storage's power limit and free capacity. Whatever the storage can't take goes to the cooling towers.
3. Remaining demand draws from storage, if temperatures allow discharging, down to the outage reserve floor. During an outage the floor is ignored and the full charge is available.
4. Con Ed steam covers whatever is left.

**Why rules instead of an optimizer:** we chose rule-based dispatch because it is transparent and auditable. Every hourly decision follows the four rules above, and the simulation records each hour's direct supply, charge, discharge, steam, state of charge and heat sent to the towers, so any hour can be checked by hand. The same rules run for every option on the Storage comparison tab, so differences between options come from the hardware, not from tuning.

## How the forecast connects to dispatch

`heatsim/forecast.py` trains a gradient-boosted model (scikit-learn `HistGradientBoostingRegressor`) on three independent synthetic years and forecasts the simulation year's hourly demand a day ahead. Its inputs are hour, day of week, day of year, temperature (that hour and the 24 h mean; the synthetic values stand in for a weather forecast) and demand 24 h and 168 h earlier.

The forecast affects dispatch only through the outage reserve, the floor in rule 3. `reserve_policies()` defines five ways to set that floor for the next ride-through hours (8 h by default):

| Policy | Reserve held |
|---|---|
| Fixed worst case (no forecast) | ride-through hours x 99th percentile demand |
| ML forecast | forecast demand over the next ride-through hours, plus a 10% margin (ASSUMPTION) |
| Hour-of-day profile (no ML) | the same, using a non-ML hour-of-day average |
| Perfect foresight (upper bound) | actual demand over the next ride-through hours |
| No reserve | nothing held back |

**The dashboard default is "No reserve", so at default settings the forecast does not change dispatch.** No reserve gives the least steam in this model (see results below). The ML forecast + reserve tab simulates every policy side by side to show this, and choosing "ML forecast" under Operations makes the forecast drive the reserve.

Forecast accuracy on the synthetic test year: about 8.5% MAPE, vs 9.0% for the hour-of-day profile and 17.5% for same-as-yesterday. With 40% space heating, the ML forecast reaches 6.7% vs 22.5% for the profile.

## Run it

Use the [live demo](https://hot-takes.streamlit.app/). The assistant is enabled there (its API key is set in Streamlit Cloud secrets).

To run locally:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

Tested with Python 3.14. **TODO:** the minimum supported Python version is not pinned anywhere in the repo.

The assistant is optional locally. To enable it, create `.streamlit/secrets.toml` with:

```toml
ANTHROPIC_API_KEY = "your-key"
```

This file is in `.gitignore`; never commit it. Without a key the dashboard works normally and the chat panel says the assistant is unavailable.

## Repo structure

```
app.py                  Streamlit dashboard (entry point)
intro.py                First-load intro animation (HTML/CSS only)
assistant.py            "Ask ChelseaHeat" assistant: tools, system prompt, assumption list
heatsim/model.py        Synthetic weather and demand, outages, storage physics, hourly dispatch
heatsim/forecast.py     Day-ahead demand forecast and outage reserve policies
heatsim/finance.py      Capex, NPV, cost of heat, customer bills, CO2, water
heatsim/realdata.py     Loads the real dorm load shape (optional sidebar choice)
scripts/real_data_validation.py  Forecast test on real BDG2 dorm steam meters
data/                   Real-data results (raw downloads in data/raw/ are gitignored)
docs/                   Team research brief, organizer materials review, judging criteria,
                        technical research, slide numbers
.streamlit/config.toml  Dashboard theme
requirements.txt        Python dependencies
CLAUDE.md               Project notes for Claude Code
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

Defaults: 1.5 MW capture, 1.0 MW average demand, 12 MWh PCM on the condenser side with 2.5 MW charge/discharge power (sized to peak demand, our assumption), no outage reserve. How each number on our slides is computed: [docs/slide-numbers.md](docs/slide-numbers.md).

**Honest findings:**
- With sublinear equipment costs and no floor-space credit, storage alone pays back in about 15 years, not the 4 to 8 years estimated in our earlier brief. The case for storage rests on reliability, floor space in a Manhattan cellar, and network growth, not on simple payback. Toggle the floor-space credit in the app to see the difference.
- Holding energy back for outages doesn't pay in this model. Capture (1.5 MW) exceeds average demand (1.0 MW), so the battery is usually full when an outage starts, and any reserve mostly blocks peak shaving. The fixed 8 h worst-case rule asks for 15.2 MWh, more than the battery holds.
- The space advantage over water is real but smaller than the brief's 8x once the store sits on the hotter condenser side, where a water tank can use a wider temperature swing.

## Data provenance (read this)

- **Demand and weather are synthetic**, calibrated to figures in our research brief (1.64 peak-to-average hot water ratio from Fulton data in the Con Ed Stage 2 filing; NYC temperature normals). No metered data for 111 8th Ave or the Fulton buildings is public.
- **To use real data:** replace `synth_weather` with `load_weather_csv` (NOAA Central Park hourly), and replace the training data in `forecast.py` with metered hot water data or NREL End-Use Load Profiles (ResStock) for New York multifamily buildings.
- Heat source size (1.5 MW) and condenser water temperature (90 F) are assumptions that must be confirmed by metering, as Con Ed did at 85 10th Avenue.
- All costs are planning estimates from cited benchmarks in `docs/`, not quotes.
- The assistant does not add data of its own: it is instructed to quote only numbers from model runs or passages in `docs/`, and it shows its tool calls so each answer can be checked.

## Real-data validation

We tested the forecast model in `heatsim/forecast.py` (same features, same gradient-boosted regressor) on real hourly metered steam from dorm buildings ("Lodging/residential") at two US Eastern-time sites in Building Data Genome 2 (BDG2), the open release of the ASHRAE Great Energy Predictor III data. We trained on 2016 and forecast 2017 one day ahead. Error is WAPE (total absolute error divided by total load; lower is better).

| Series | Our ML | Same as yesterday | Hour-of-day profile |
|---|---|---|---|
| Cockatoo site, 7 dorm meters summed | 0.180 | 0.243 | 0.388 |
| Eagle site, 3 dorm meters summed | 0.304 | 0.350 | 0.363 |
| Median of the 10 individual dorms | 0.297 | 0.330 | 0.429 |

Caveats:
- This is dorm steam, which includes space heating. It is not NYCHA apartment hot water, and no metered data for the Fulton Houses was used.
- WAPE on real data is not comparable with the 8.5% MAPE on our synthetic year. Real loads are much harder to forecast than our synthetic ones.
- The ML model beats both baselines on the summed series and on the median dorm, but loses to the hour-of-day profile on 3 of the 10 individual dorms. On this real data, same-as-yesterday beats the hour-of-day profile, the reverse of our synthetic result.
- The reserve-policy results above still use synthetic data.

Reproduce with `.venv\Scripts\python scripts/real_data_validation.py`. It downloads the raw BDG2 files into `data/raw/` (gitignored, never committed) and writes `data/real_steam_results.csv`, which the app's ML tab reads. The app itself never downloads or trains on this data.

**Run the model on a real load shape.** The sidebar's "Demand data" choice switches from the synthetic default to "Real metered shape (BDG2 dorms)": hourly summed steam for the 7 Cockatoo dorms in 2017, with that site's air temperature, rescaled to the average-demand slider (our assumption: the shape scales linearly). The forecast then trains on the same dorms' 2016 data. This is dorm heating plus hot water, not NYCHA data, so results differ from the synthetic numbers above, which are what our deck and this README quote. The data is in `data/real_demand_cockatoo.csv` (gaps filled as described in the script; a `filled` column marks them). The "Ask ChelseaHeat" assistant always uses the synthetic data.

Dataset: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. *The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition.* Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x. Data from [github.com/buds-lab/building-data-genome-project-2](https://github.com/buds-lab/building-data-genome-project-2), licensed CC BY-SA (Creative Commons Attribution-ShareAlike; see that repo's LICENSE). Files in `data/` derived from it are shared under the same license.

## Limitations

- Demand and weather are synthetic, so forecast errors mostly reflect the noise we injected, and every result inherits the calibration to the brief.
- Key inputs are our assumptions until metered: 1.5 MW capture, 90 F condenser water, 2.5 MW storage power and the 87 to 65 F condenser-side tank swing.
- The model has one heat source (one tenant's condenser loop) and one aggregate demand profile. Commercial buyers appear only as a price and share in the finance model.
- Dispatch follows fixed rules, so results show what those rules achieve under each design.
- AI answers can be wrong; check the tool calls shown under each answer. Questions and model results are sent to Anthropic's API to produce answers.

## Team

3-person team, NYU Sustainable Data Center Hackathon 2026.

Built with help from [Claude Code](https://claude.com/claude-code) for the simulation, app and dashboard design.
