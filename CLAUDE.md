# ChelseaHeat: NYU Sustainable Data Center Hackathon (Grundfos Waste Heat Reuse Challenge)

## Project
Proposal for Site 1, 111 8th Ave (NYC). A phase change (salt hydrate, ~84 F melt) thermal
battery at 111 8th Ave feeds data center heat into Con Ed's Chelsea thermal network,
serving hot water to the rebuilt NYCHA Fulton Houses. Research basis: docs/ (team brief).

## Code
- heatsim/model.py: 8,760-hour simulation (supply, demand, storage, outages, steam backup)
- heatsim/forecast.py: gradient-boosted day-ahead demand forecast that sets the outage reserve
- heatsim/finance.py: capex, NPV, cost of heat, customer bills, CO2, water
- app.py: Streamlit demo for judges. Run: python -m streamlit run app.py

## Conventions
- All power values are SOURCE-SIDE heat in MW thermal (heat taken from the data center).
  Delivered heat = source * COP/(COP-1). Never mix MW and MWh.
- Mark any number that is our own assumption with "ASSUMPTION" in comments and the app.
- Demand and weather data are SYNTHETIC, calibrated to the brief. Never present them as real.
- Never invent data, citations, or results.

## Key findings to keep consistent (defaults; reproduce in the app before quoting)
- PCM on the shared ambient loop barely charges in winter (steam ~325 MWh/yr, 96.3% served);
  on the condenser water side it serves 99.9% (steam ~10 MWh/yr vs ~393 with no storage).
- Storage power is sized to peak demand (2.5 MW, ASSUMPTION), not to capture (1.5 MW); at
  1.5 MW, outage steam is power-limited, not energy-limited.
- Holding an outage reserve does not pay in this model: no reserve ~10 MWh/yr steam, perfect
  foresight ~20, ML forecast ~33, hour-of-day profile ~37, fixed 8 h worst case ~185 (it asks
  for 15.2 MWh, more than the 12 MWh battery). The battery is usually full when outages start.
- ML forecast MAPE 8.5% vs 9.0% for a non-ML hour-of-day profile and 17.5% for persistence
  (synthetic data, so near the injected noise). With 40% space heat: 6.7% vs 22.5%.
- Water tank needs ~7.8x the PCM floor area on the loop side (5.6 C swing) but only ~3.5x on
  the condenser side (87 to 65 F swing, ASSUMPTION). Use the condenser-side figure for the
  revised design.
- Storage simple payback ~15 yr with sublinear capture costs and no floor credit; case rests on
  reliability and space.

## Rules
- Keep the app runnable at all times. Test with python -m streamlit run app.py after changes.
- Small, focused changes. Explain what you changed and why.