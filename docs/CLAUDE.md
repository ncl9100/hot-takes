# ChelseaHeat: NYU Sustainable Data Center Hackathon (Grundfos Waste Heat Reuse Challenge)

## Project
Proposal for Site 1, 111 8th Ave (NYC). A phase change (salt hydrate, ~84 F melt) thermal
battery at 111 8th Ave feeds data center heat into Con Ed's Chelsea thermal network,
serving hot water to the rebuilt NYCHA Fulton Houses.

## Code
- heatsim/model.py: 8,760-hour simulation (supply, demand, storage, outages, steam backup)
- heatsim/forecast.py: gradient-boosted day-ahead demand forecast that sets the outage reserve
- heatsim/finance.py: capex, NPV, cost of heat, customer bills, CO2, water
- app.py: Streamlit demo for judges. Run: python -m streamlit run app.py

## Research (read before making technical or financial claims)
- docs/team-brief.md: our design basis (site, offtakers, PCM battery, costs). Header lists
  figures our model revised. docs/team-brief.pdf is the original.
- docs/judging-criteria.md: hackathon rubric and the challenge brief's evaluation areas
- docs/organizer-materials-review.md: summaries of all organizer source materials
- docs/technical-research.md: key technical findings (short)

## Conventions
- All power values are SOURCE-SIDE heat in MW thermal (heat taken from the data center).
  Delivered heat = source * COP/(COP-1). Never mix MW and MWh.
- Mark any number that is our own assumption with "ASSUMPTION" in comments and the app.
- Demand and weather data are SYNTHETIC, calibrated to the brief. Never present them as real.
- Never invent data, citations, or results.

## Key findings to keep consistent
- PCM on the shared ambient loop barely charges in winter; placement moved to condenser water side.
- ML forecast reserve beats a fixed 8 h reserve (steam ~37 vs ~190 MWh/yr at defaults).
- Storage payback ~16 yr with sublinear capture costs; case rests on reliability and space.

## Rules
- Keep the app runnable at all times. Test with python -m streamlit run app.py after changes.
- Small, focused changes. Explain what you changed and why.
