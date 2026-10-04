# Organizer Materials Review (cumulative, complete)

All 24 organizer items reviewed as of 2026-10-03. Tags: [Source] claim by the document; [Check] arithmetic or consistency check; [Analysis] Claude's interpretation; [Unverified] background knowledge not yet confirmed. Same content as Section 3 of the team context file.


Started and completed October 3, 2026. All 24 organizer items are now reviewed: root-level files (3.2 to 3.8), then the Grundfos Challenge folder, Presentations, White Papers, New York State folder and the iMasons transcript (3.9 to 3.25), followed by updated cross-cutting findings (3.26). The organizer Google Drive folder mirrors the local "Source Documentation" folder; Drive search only indexed some files, so the remaining files were read from the identical local copies.

## 3.1 Source inventory

| # | Section | File | Status | Depth |
|---|---|---|---|---|
| 1 | Root | 20230623 Data Centers HeatReuse 101 3.2 (OCP, 14 pp) | Reviewed | Full text; figures read from text and captions |
| 2 | Root | NYU BAC Hackathon_HDR_Waste Heat Reuse_2026.1002 (HDR deck, 69 pp) | Reviewed | Full text plus visual review of ~45 chart/diagram pages |
| 3 | Root | Topic 5 - Heat reuse, Connecting DC to DE systems_v5 (Grundfos, 44 slides) | Reviewed | All slide text, speaker notes, and rendered visuals of slides 5 to 41. Slide 31 is an embedded video (FRA-Mainz), not viewable |
| 4 | Root | district-energy-application-guide (Grundfos, 2018, 29 pp) | Reviewed | Full text; diagrams via captions and chart labels |
| 5 | Root | iGRID Playbook (Grundfos internal sales playbook, 243 pp) | Reviewed (partial depth) | Read: intro and market trends (pp 1-38), value proposition (79-100), personas (101-123), iGRID concept, products, software, services, competitors, success stories (140-243). Skimmed only: regional market pages (48-78) and internal sales-org pages (124-139) |
| 6 | Root | Williams_College_and_the_Geothermal_Earth_Battery.m4a (18.8 min audio) | Reviewed (3.21) | Via uploaded transcript |
| 7 | White Papers | CBS_Data_center_white_paper_DISTRICT HEATING (Grundfos/Siemens, 22 pp) | Reviewed (3.12) | Full text |
| 8 | White Papers | Colocating-Data-Centers_Greenhouses-RII-Virginia (54 pp) | Reviewed (3.16) | Main report and Agriport A7 appendix; interview appendix skimmed |
| 9 | White Papers | DATA HEAT - Sector Coupling ... Market Development Guide (3MAR26, 159 pp) | Reviewed (3.17) | Main report and NY-relevant appendix pages; general policy appendix skimmed |
| 10 | White Papers | Danfoss Waste Heat (Impact No. 9, 28 pp) | Reviewed (3.13) | Full text |
| 11 | White Papers | Danfoss White Paper Sample (Impact No. 3, cities) | Reviewed (3.14) | Heat, DC and sector integration chapters; transport chapters skimmed |
| 12 | White Papers | Developing Community and Data Center Synergies With District Energy - CenTrio (16 slides) | Reviewed (3.24) | Slide text; diagrams image-only |
| 13 | White Papers | Every Drop Counts - Grundfos Water Scarcity Paper 2026 | Reviewed (3.15) | DC and industry sections; agriculture/utility sections skimmed |
| 14 | White Papers | US Policy Landscape Data Center Heat Reuse - David Gardiner & Associates (8 slides) | Reviewed (3.23) | Slide text; state map image-only |
| 15 | White Papers | driving_sustainable_data_centres-AD Highlighted (38 pp) | Reviewed (3.18) | Heat, water, policy sections; ESG/back-office sections skimmed |
| 16 | Presentations | NYU_Data_Center_Heat_Reuse_Hackathon_Deck_Challenge and Workshop - opening slides (13 slides) | Reviewed (3.10) | Slide text and speaker notes |
| 17 | New York State | IDEA - Thermal Energy Storage for Data Centers_CB and I (19 slides) | Reviewed (3.19) | Full text |
| 18 | New York State | June 10th FPCJ Meeting Summary Compiled (24 pp) | Reviewed (3.20) | Full text |
| 19 | New York State | Resource Efficient Decarbonization (NYSERDA EBC, 69 pp) | Reviewed (3.22) | Framework and all 10 project summaries |
| 20 | New York State | urbs Williams College Energy Transition Strategy ver1.0 (17 pp) | Reviewed (3.21) | Full text |
| 21 | Grundfos Challenge | NYU_Hackathon_Data_Center_Heat_Reuse_Challenge_R1.docx | Reviewed (3.9) | Full text |
| 22 | Grundfos Challenge | Suburban Site - Lake Hawkeye (HDR, 39 pp) | Reviewed (3.11) | Captions plus input panel; maps image-only |
| 23 | Grundfos Challenge | Urban Site - 111 8th Ave (HDR, 39 pp) | Reviewed (3.11) | Captions plus input panel; maps image-only |
| 24 | Project only | Transcript from Great podcast on heat reuse by iMasons | Reviewed (3.25) | Full text (auto-captions) |

## 3.2 OCP "Data Centers Heat Reuse 101" (Open Compute Project, June 2023; Alfa Laval, Cloud&Heat, NREL)

**Key arguments [Source]**

- Almost 100% of server energy becomes heat; in theory all of it (IT, power losses, chiller thermodynamics) can be captured.
- Heat reuse has existed 10+ years but has not scaled even in the Nordics. Six barriers: hard-to-replicate local conditions (distance, new pipe cost), climate dependence, unhelpful legislation, no general subsidies, hard DC/host collaboration, high system energy and capex (pipes, pumping stations, heat pumps, controls).
- What changed: government decarbonization mandates and subsidies, corporate net-zero goals, higher fossil fuel prices, and liquid cooling raising return temperatures.
- Preconditions: a nearby heat host (or a utility as intermediary), a useful temperature, ideally shared ownership (campus), supportive legislation.
- Ideal hosts have high, constant, defined 24/7 demand: water preheat, industrial laundries, bio-ethanol, food and beverage, breweries, large hospitals, desalination and wastewater treatment, chemical/textile/metal, pharma. Seasonal hosts: district heating, biomass drying, greenhouses, fish farming. Table 1 maps hosts to density classes (high-density urban: private DE, district energy, HVAC reheat, pools, hospitals/hotels, wastewater).
- Cost allocation principle: extraction costs split between DC and host; transformation costs (storage, temperature lift, heat-to-cooling) paid by the host. Heat should be free or cheaper than the host's alternative.
- Carbon accounting: avoided emissions belong to the heat host; the DC only gets credit via its own energy savings unless compensated contractually.
- Water: reuse lowers chiller/cooling tower use, avoiding evaporation.
- Heat reuse rarely reduces DC capex, only opex; DCs keep redundant cooling regardless.
- Techno-economics are site specific: heat quantity and temperature, pipe distance or existing network, geography, CO2 and water benefits, evaluated on a life-cycle basis.
- Proposed next step: an OCP matchmaking platform plus checklists, maps and TCO tools.

**Quantitative values [Source]**

- Return temperatures: air ~27-28 °C; liquid cooling 45-65 °C. Figure 3 scale: air cooling to ~28 °C, rear door HX ~28-40 °C, cold plate and immersion 40-65 °C.
- DC uptime >99.8% yearly, "maximum 20 h downtime per year". [Check] 0.2% of 8,760 h = 17.5 h, so 20 h is a rounded upper bound.
- Containerized/modular DCs can exceed 0.5 MW.

**Industry needs revealed [Analysis]**: DCs need a reliable offtaker and will not risk cooling; hosts need cheap, continuous, temperature-matched heat; both need a broker or utility and a clear commercial and carbon-credit split. The lack of a structured way for producers and consumers to find each other is named as "one of the biggest challenges".

**Dated or weak points**: 2023, pre-AI-density boom; cites a 2022 fuel-price spike as a driver; no cost numbers at all.

## 3.3 HDR "Data Center Waste Heat Reuse Resource Presentation" (updated 2026-10-02)

**Structure**: DC fundamentals and market; performance metrics; cooling fundamentals; waste heat reuse ("heat export"); energy-water nexus; carbonate fuel cells; embodied carbon (MEP 2040); hyperscaler goals.

**Market data [Source]**

- Visual Capitalist (Feb 2026): 10,807 DCs globally; USA 3,960 (~37%), GBR 498, DEU 470, CHN 365, FRA 335.
- NLR (DOE lab, March 2026) map of US DC infrastructure with transmission and gas pipelines; clusters in Virginia, Texas, Ohio, Georgia, Arizona.
- CBRE 2025: power availability is the prime growth constraint; Q1 2025 global vacancy 6.6%; pricing $217.30/kW/month (+3.3%); operators "quickly adopting liquid cooling".
- JLL: Texas could overtake Virginia by 2030 (Virginia ~8 GW existing + ~4 GW under construction; Texas ~4.5 + ~6.5 GW, read from chart).
- Uptime: average PUE 2.50 (2007), 1.58 (2014), flat at ~1.54-1.59 since 2020; 2025 = 1.54. PUE falls with size: 1.69 (<99 kW) to 1.44 (>=20 MW).

**Metrics [Source]**

- PUE; WUE (industry average site WUE 1.8 L/kWh); CUE; ERE = (total facility energy minus reuse energy) / IT energy; ERF = reuse energy / IT energy.
- Worked example (St. Louis): IT 1,000 kWh, facility 1,300 kWh (PUE 1.3), 200 kWh reused gives ERE 1.1. [Check] (1300-200)/1000 = 1.1 and ERF = 0.2. Correct.
- Green Grid DCRE v1 combines PUE, WUE, water stress, Water Usage Impact (WUI = site water x water stress factor, standalone since 2025), climate zone, water source. Example scores ~1.19-1.30 depending on maturity level.
- Conceptual metrics: EUI (grid impact of AI loads: spiky training loads, harmonics, sudden load drops; AI gigascale peak from grid 60-90% with onsite generation) and ITWC (useful compute per energy).
- There is no heat reuse term in DCRE as shown. [Analysis] That is a gap a heat-reuse proposal can point to.

**Rack density [Source]**: low <5 kW up to extremely high 160-320 kW (AI clusters); air close-coupled rack cooling up to ~60 kW/rack; two-phase D2C >2,000 W per chip with 4-9x lower flow than single-phase.

**Temperature map (slide 42, °F, values read from chart, approximate) [Source]**

| Item | °F | ≈ °C |
|---|---|---|
| D2C supply water | ~96-108 | 36-42 |
| D2C return water | ~102-113 | 39-45 |
| Immersion liquid supply | ~110-120 | 43-49 |
| Immersion liquid return | ~120-157 | 49-69 |
| Cooling tower return (from chiller) | ~85-92 | 29-33 |
| Radiant heating HWS | ~85-120 | 29-49 |
| AHU coil HWS | ~120-180 | 49-82 |
| Condensing gas boiler HWS | ~125-180 | 52-82 |
| Air-cooled HP HWS, standard / "Empire Tech" | ~120-140 / ~140-165 | 49-60 / 60-74 |
| Water-cooled HP HWS, standard / "Empire Tech" | ~125-155 / ~155-175 | 52-68 / 68-79 |
| Single-effect absorption chiller HWS, process heat | 200-220 | 93-104 |

[Analysis] This is the most useful chart in the root folder for supply/demand temperature matching: D2C return heat can directly serve radiant/low-temperature hydronic systems, but reaching AHU coils or legacy boiler loops needs a heat pump; immersion return overlaps the low end of AHU and condensing-boiler ranges.

**Heat reuse framing [Source]**

- Equinix heat export: servers warm water to ~25-30 °C, heat exchanger to a second loop, heat pump raises to ~60-90 °C, delivered to homes, offices, pools, greenhouses, industry.
- Urban / suburban / rural DC environments shown side by side (matches the hackathon's two site types).
- Industrial symbiosis principles; DHC generations 1G to 5G (5G ambient loops shown as 23-77 °F on one slide and 41-95 °F on the next).
- HDR Thermal Energy Network (TEN) concept: DC, industry and wastewater as sources; hospital, science, CRE, higher ed, sports, civic, justice as sinks; central GeoExchange borefield (>400 ft, ~50 °F ground year-round), wastewater energy recovery, central heat pump chillers; buildings can be both source and sink.
- Community pushback ("No Data Centers" photo); heat island graphics claiming DCs raise temperatures "up to 16 °F" and "6 miles away affecting 343 million people".
- Grundfos "TCO iceberg" for DE pumping: purchase price ~5% of TCO; energy up to 85% of lifetime cost; poorly specified pumps use 10-20% more energy; modern controls cut it 20-60%.
- **Trade condition (slide 51) [Source]**: user buys if offer price Y < its current heat cost X; provider sells if Y > its cost to reject heat Z, where Y also covers the cost to upgrade and distribute. [Analysis] This is a ready-made economic model: a deal exists only when Z < Y < X.

**Water [Source]**: cooling tower water = evaporation 67%, blowdown 32%, drift <1%; cooling tech ranked high / low-moderate / zero water (heat export listed as zero water); a site water budget example of ~2.2 million liters of cooling tower makeup that disappears without towers; US power generation consumes ~2 gal/kWh (withdraws ~12).

**Fuel cells [Source]**: FuelCell Energy carbonate blocks (1.25 MW each, scalable to 500 MW+), 725 °F exhaust for absorption chilling; CO2 1,393 lb/MWh (US non-baseload grid) vs 886 (FCE electric only), 555 (with heat recovery), 133 (with carbon capture, under development); water 0.13-0.19 gal/kWh vs 0.47 for DC average; 30% US ITC through at least 2032. HDR tool example (Seattle, 20 kW/rack, 75% load): 18 x 1.25 MW SOFC, 169.9 GWh/yr, absorption cooling covers 474.6 million kBTU/yr, total efficiency 86.5%, heat recovery 0 because heating load is 0. [Check] 169.9 GWh / 8,760 h = 19.4 MW average vs 22.5 MW rated (86%). [Analysis] HDR treats onsite "behind-the-meter" power as a heat source too; the exhaust is far higher grade (~700 °F) than IT heat.

**Embodied carbon [Source]**: MEP 2040; building A1-A3 473 kgCO2e/m2 (MEP 128, of which mechanical 75.3, piping 24.1); MEP whole life 1,115 kgCO2e/m2 = 460 embodied + 655 operational. [Analysis] Relevant if a proposal adds kilometers of pipe or large heat pumps: embodied carbon of piping and refrigerant leakage (B1.2 refrigerants = 77) should appear in a carbon claim.

**Industry needs revealed [Analysis]**: power is the binding constraint for DC growth; community acceptance is a real project risk; the industry is shifting metrics from efficiency (PUE) to impact (water stress, grid stress); HDR as designer thinks in campus-scale TENs with multiple sources and sinks.

**Weak or questionable content**: many illustrations are AI-generated (labeled). Heat island statistics come from social-media style graphics with no primary citation. Slide 53 mixes units ("0.4-0.6 gallons/kWh" headline, "0.4-0.6 L/kWh" subtitle). Fuel cell slides are vendor marketing.

## 3.4 Grundfos "Topic 5: Heat reuse, connecting DC to DE systems" (CPD training deck)

**Key arguments [Source]**

- AI is driving more build in 3 years than the past 30; $3T+ investment projected by 2030; 373 GW global capacity (71 active, 22 under construction, 280 pipeline); 11,800 DCs.
- Constraints: power (time to power), pushback ($150B of projects blocked or delayed in 2025), people (80,000+ US electrician openings/yr), planet (behind-the-meter fossil power), policy.
- Rack density path 10 kW to 150, 250, 600, >1,500 kW; shift to closed-loop D2C and "zero water".
- 95-100% of DC energy becomes heat; "up to 85% recoverable".
- Temperatures: air ~25-35 °C, liquid ~35-60 °C, immersion >60 °C.
- Pain points: temperature mismatch, distance to demand, commercial alignment (who pays, who benefits), reliability concerns, joined-up legislation/planning/specification.
- Benefits list: lower PUE / optimized WUE / higher ERF, ESG, absorption cooling, faster approvals and community positioning; ROI "typically 1.5-4.0 years"; "each MWth of recovered heat avoids ~1,770 t CO2/yr".
- ~90% of DH heat still from fossil fuels (IEA). DH generations 1G to 4G (4GDH 50-60 °C flow, two-way, prosumers) and 5G ambient loops with bidirectional flows, storage, DCs as continuous sources.
- Heat pumps: COP 2-5, falling as lift rises; 20-40 °C lift is "ideal"; "no heat reuse project without heat pumps".
- Five configurations (from Trade Council of Denmark / IDEA / NY State "State of Opportunity"): **Ambient** (DC heat into ~20-40 °C TEN, building-level heat pumps), **Centralised** (heat pump at DC "energy data center", hot network), **Hybrid**, **Chip heating** (DC delivers ~45-50 °C directly, no heat pump), **Indirect** (DC rejects into district chilled water return; heat pumps on the DCHW loop).
- Impact claims: >10 Mt CO2/yr avoidable in Europe; waste heat could supply ~10% of heat demand; up to €1M/yr DC revenue; regulations targeting 10-20% heat reuse by 2026-2028.

**Case studies [Source]**

- UK university campus (photo is Edinburgh's Old College, name not stated): peak ~11 MW campus; 300 kW heat pump; evaporator 25 to 16 °C, condenser 60-75 °C; COP 2.95; pump efficiency 86%; shunt and booster pumps for stable injection.
- Høje Taastrup, Denmark (hyperscaler): DC heat ~30 °C supply / 15 °C return; heat pump lift; 33,000 MWh pit storage; 6,000 homes; 25% of 310 GWh network demand.

**Checks [Check]**

- Campus COP: Carnot limit with ~16 °C source and ~75 °C sink is ~348/59 ≈ 5.9, so 2.95 is ~50% of Carnot. Plausible.
- Høje Taastrup: 25% x 310 GWh ≈ 78 GWh/yr; 78 GWh / 6,000 homes ≈ 13 MWh per home. Internally consistent.
- 1,770 t CO2/MWth: 1 MWth x 8,760 h = 8,760 MWh; at ~0.2 t CO2/MWh heat from gas boilers that gives ~1,750 t. So the claim assumes full-load 8,760 h, gas displacement, and gross (not net of heat pump electricity) savings. Not transferable to a NYC case without a local emission factor and heat pump electricity accounting.
- Capacity slide: "USA current capacity 228 GW" exceeds the slide's own "global active 71 GW". Internally inconsistent; at least one figure is wrong or uses a different definition.

**Industry needs revealed [Analysis]**: Grundfos sees the DC as one of many sources in a heat-pump-centred network; its value story is hydraulic: stable injection (shunt/booster pumps), storage, control. The configuration slides are the clearest statement of the design choices the brief expects us to make.

## 3.5 Grundfos District Energy Application Guide (2018)

**Key content [Source]**

- DH flow/return typically ~75/35 °C; low temperature 60/30 or 55/25 °C. District cooling ~10/20 °C (older 4/12 °C).
- Peak heating and cooling loads of a building are often similar, but heating lasts ~3x longer in northern Europe.
- Direct vs indirect connection: direct allows lower temperatures but max ~6 bar; indirect needs ~10 °C higher flow and return and a pump per building but gives hydraulic separation. Brazed plate HX up to ~2 MW; gasketed 30-50 MW. Secondary temperature adjustment saves up to 20%.
- Tariffs: fixed (capital, O&M), variable (energy, including purchased surplus heat), connection fee; incentives for low return temperature or penalties for high.
- Smart meters measure flow and both temperatures; combined with SCADA give full system picture.
- **Hydraulics**: Φ = Q x Δt; a 1.5 °C Δt increase gives 20% less flow; affinity laws: 50% speed gives 25% head and 12.5% power; raising Δt by 1 °C (cooling) or 3 °C (heating) cuts hydraulic power ~27%; design pressure loss ~100 Pa/m; diversity factor as low as 0.65.
- TERMIS temperature optimization: ~10% heat loss reduction, up to 2% of heat cost.
- CHP: ~35% electric + 60% heat = 95% vs ~45% for condensing plant.
- Surplus heat must match DH temperature; options: stepwise heat exchangers, heat pumps, or use as preheat.
- TVIS case (Denmark): 140 km transmission, 80,000 homes; 55% CHP, 26% refinery surplus heat, 11% waste incineration, 2% peak boilers.
- Storage: stratified tanks, pit storage (lifts solar share to ~50% of annual demand), aquifers.
- **Bjerringbro case (Grundfos factory + utility, 2013)**: compressor condenser heat; summer heat stored in an aquifer ~750 m away, ~80% recoverable in autumn; utility heat pump lifts temperature; Grundfos saves up to 90% of cooling tower power; €4.7M invested, split 50/50; ~€0.4M/yr savings; payback 12-13 years ("fine for a DH company, often too long for an industrial company"); 3,700 t CO2/yr.
- Denmark: ~64% of homes on DH; 80% of DH from CHP.

**Industry needs revealed [Analysis]**: a utility judges a heat source by return-temperature impact, Δt, pumping energy and storage flexibility, not just by MWh. The Bjerringbro case is the closest documented analogue to a DC-to-DH project in these materials (waste heat from cooling machinery, seasonal storage, heat pump at utility side, 50/50 cost split, different payback tolerances for each party).

**Dated points**: 2018; Danish/European context; no data-center-specific numbers.

## 3.6 Grundfos iGRID Playbook (internal sales playbook, ~2024)

**What it is**: a sales enablement document for Grundfos's District Energy vertical. It explains how Grundfos sells, to whom, and what customers care about. Data Centers is listed as a separate Grundfos vertical.

**Market [Source]**

- DH ~9% of global building/industry heat (2022); ~90% fossil; ~4% of global CO2; 40% renewable/waste heat by 2040 expected; DH growth ~4%/yr, district cooling 7-9%/yr. Cooling 20% of world electricity rising to ~40% by 2050.
- North America is "mostly campus heating systems (universities, hospitals, military, airports)"; residential is individual. US market has a high share of combined heating and cooling; "conversion from steam to hot water in campuses, hospitals and army barracks is a key driver for the US market" (Danfoss VP quote).
- Regional deep dives cover Europe, IMEA, China only, not North America.
- Barriers: high capex, lack of awareness and skills, split incentives, retrofit cost, regulatory uncertainty, customer perception.
- 5GDHC trends: near-groundwater temperatures, bidirectional, decentralized. Example: UK £36M grant for West London DH using DC waste heat for up to 10,000 homes (Nov 2023).

**KPIs utilities track [Source]**: system efficiency (DH 0.7-1.2 kW/kW target; district cooling 0.55-0.7 kW/RT); supply/return: HTDH 90-120/60-80 °C, LTDH 60-80/30-50 °C, district cooling 4.5-6/14.4-16 °C; uptime (MTBF, MTTR), heat losses, water leakage, cycles of concentration, ROI, lifecycle cost, capex/opex, TES, demand-side management.

**Customer personas [Source]**: Contractor (on time, no penalties); End-user/Utility, the key decision maker (lowest opex, balance supply and demand with flexibility, cut fossil use, reliable delivery, expand without affecting existing customers, reduce fresh water, network insight, future-proofing); Designer/Consultant (feasibility, predict consumption patterns, cost-effective compliant design, layout optimization, futureproof, right energy sources); Operation Manager (uptime, maintenance scheduling, fast alarms, balanced contractual flow/pressure/temperature, fast connection of new customers).

**iGRID [Source]**: splits grids into demand-driven temperature and pressure zones. Temperature Zone = prefabricated mixing loop blending return into supply; heat loss reduction "typically 20-30%", "up to 25%", "up to 30%", case claim "estimated 50%"; payback ~3.5 years. Pressure Zone = distributed variable-speed booster pumps. Pit Measure Point powered by a thermoelectric generator using supply/return ΔT, GSM to cloud. Temperature Optimiser = weather compensation (outdoor temp, wind) plus peak shaving (pre-loading heat into pipes before peaks). Data analytics on heat-meter data to find buildings with high return temperatures, then building balancing visits. Cases: Chinese city (7.2% heat savings, 4.9% less leakage, 8.53% pump energy), Danish utilities (80-100 to 60-65 °C), OPEC Gdynia (984 GJ loss reduction, tradable white certificates).

**Industry needs revealed [Analysis]**: this is the best evidence in the folder of what Grundfos (the challenge sponsor) values: lower network temperatures to admit low-grade sources like DC heat, low return temperatures and high Δt, distributed pumping, real-time data, predictive control and measurable payback. A low-temperature DC heat source is exactly the use case iGRID-style zoning is built for.

## 3.7 Williams College Geothermal Earth Battery (audio)

Reviewed from the uploaded transcript together with the urbs Williams College document; see 3.21.

## 3.8 Cross-cutting findings after the root-level files (superseded in part by 3.26)

### Recurring technical constraints [Source, multiple documents]

1. **Temperature mismatch is the core problem.** Air-cooled DC heat is ~25-35 °C; existing DH wants 60-120 °C. Liquid cooling (35-65 °C) narrows the gap; heat pumps close it at COP 2-5.
2. **Continuity vs seasonality.** DC heat is flat 24/7; heating demand is seasonal (OCP; DE guide's 3:1 heating vs cooling duration; Høje Taastrup storage). Storage (pit, tank, aquifer) or year-round sinks (DHW, pools, process, greenhouses) resolve it.
3. **DC cooling reliability is non-negotiable.** DCs keep redundant heat rejection (OCP); hosts need backup when DC heat drops.
4. **Hydraulics matter to Grundfos.** Return temperature, Δt, pump energy, pressure zoning, and stable injection (shunt and booster pumps) recur in all three Grundfos documents.
5. **Economics hinge on the counterfactual.** Heat must be cheaper than the host's alternative and worth more than the DC's rejection cost (HDR Z < Y < X; OCP).
6. **Ownership split.** OCP: extraction split, transformation paid by host. Bjerringbro: 50/50 split. Utility as intermediary is a recurring model.

### Contradictions and inconsistencies

| Topic | Values | Sources |
|---|---|---|
| Number of DCs | 10,807 (USA 3,960) vs 11,800 (USA 5,381) | HDR vs Topic 5 |
| Capacity | "USA 228 GW" vs "global active 71 GW" | Topic 5, internal |
| Liquid cooling temperatures | 45-65 °C vs 35-60 °C vs D2C return ~39-45 °C | OCP vs Topic 5 vs HDR |
| Immersion | ">60 °C" vs return ~49-69 °C | Topic 5 vs HDR |
| 4GDH temperature | 55-60 °C flow vs 50-60 °C vs 122-158 °F (50-70 °C) vs "<70 °C" vs LTDH 60-80 °C | DE guide, Topic 5, HDR, iGRID |
| 5GDH temperature | 23-77 °F vs 41-95 °F vs ambient loop 20-40 °C | HDR (two slides) vs Topic 5 notes |
| Payback | 1.5-4 years (generic) vs 12-13 years (Bjerringbro) vs ~3.5 years (iGRID zones, a different product) | Topic 5, DE guide, iGRID |
| iGRID heat loss reduction | 20-30%, up to 25%, up to 30%, ~50% | iGRID, internal |
| Water per kWh | site WUE 1.8 L/kWh vs "0.4-0.6 gal/kWh (0.4-0.6 L/kWh)" | HDR internal (1.8 L ≈ 0.48 gal, so the gallon figure matches and the L label looks like an error) |
| Who gets carbon credit | Host only (OCP) vs heat reuse "improves DC ESG metrics" (Topic 5) | Both can be true if ERF/ERE is reported separately from avoided CO2 |

### Outdated or weakly sourced

- Topic 5 slide 12 uses a 2015 MDPI projection (1,137 / 2,967 / 7,933 TWh by 2030); widely regarded as overestimated. Treat as historical, not current. [Unverified: newer IEA estimates are far lower; confirm before citing]
- OCP paper is 2023 and has no costs. DE guide is 2018.
- "10-20% heat reuse requirements by 2026-2028" is European. [Unverified: this matches Germany's Energy Efficiency Act; confirm, and check whether any NY or US rule exists, likely in the David Gardiner policy paper]
- Heat island figures in the HDR deck lack primary sources; do not cite.

### Implications for our approach (not a project idea yet)

- The brief's required "matching by temperature, capacity, timing, seasonality and continuity" maps directly to the HDR temperature chart, the Topic 5 configuration diagrams and the DE guide hydraulics. Any solution should show this matching quantitatively, hour by hour across a year.
- Grundfos judges will likely respond to: heat pump COP vs lift, Δt and return temperature, pump energy, storage, controls and real-time data. A purely "map of sources and sinks" concept would underuse what the sponsor cares about.
- The Z < Y < X trade condition plus OCP's cost split gives a defensible economic and ownership framework to quantify.
- Carbon claims must be net of heat pump electricity, use a local grid factor, and respect OCP's credit-allocation point. The 1,770 t/MWth figure should not be reused uncritically.
- Configuration choice (ambient, centralized, hybrid, chip, indirect) is likely site dependent: urban 111 8th Ave vs suburban Lake Hawkeye. The NYS documents and site profiles are needed to decide.
- In the US, DE is mostly campus-scale, which makes campus or TEN-style sinks more realistic than a city-wide hot-water DH network.

### Open questions after the root-level files (see 3.26 for which are now resolved)

1. Site engineering data for both sites (IT load, cooling type, temperatures, PUE). Still missing.
2. What thermal networks exist near each site? [Unverified: Manhattan is served by Con Edison's large steam system, a 1st-generation network that low-grade DC heat cannot feed directly; confirm in NYS materials]
3. NY policy: does New York's thermal energy network legislation (TENs) apply? [Unverified]
4. What is HDR's "Empire Tech" heat pump category? Possibly linked to NYSERDA's Empire Building Challenge. [Unverified]
5. Applicable NYC/NY grid emission factor and gas price for the counterfactual.
6. Does any material provide heat pump cost per kW, pipe cost per meter or storage cost? None so far.
7. Williams College audio content (needs transcript).

## 3.9 Challenge brief R1 (Grundfos Challenge folder)

**Full design questions [Source]**

- **Site 1, Urban: 111 8th Avenue Data Center (commissioned).** 111 8th Ave, New York, NY 10011. Operator described as a "multi-tenant carrier hotel and data center facility". Design question: how can the data center become a reliable thermal energy hub for the most suitable local heat offtakers? Consider: justify offtakers; match supply and demand by temperature, capacity, timing, seasonality and continuity; heat upgrading, distribution and building interfaces; backup heat and continuity without compromising data center cooling reliability; costs, risks, ownership and responsibilities.
- **Site 2, Suburban/Residential: Lake Hawkeye Data Center (proposed).** Former Cayuga Power Plant site, Lansing, NY. Developer/operator: TeraWulf. Design question: how can recovered heat reliably serve the most suitable nearby residential and community heat users? Consider: justify offtakers; same matching criteria; domestic hot water, building heating and community facilities; heat pump needs, distribution and backup heat; affordability, community acceptance and continuity of supply.
- The challenge framing says "two site scenarios", but the deliverable says "Select one setting and justify why the proposed solution is appropriate for that local context."
- Resources promised to students that we have NOT found in the folder: community impacts and mitigation presentation; public data-source list with GIS resources; data center cooling and temperature terminology; mapping, land-use, utility, building-energy and demographic datasets. [Check] Worth asking organizers.

## 3.10 Opening slides: "Challenge and Workshop" (Presentations folder)

**Content [Source]**

- Hackathon support team: HDR (Director of High-Performance Design; Data Centers Business Development Lead) and Grundfos (Global Sales Development, Data Centers, CBS Americas; Data Centers Business Development Lead; Chief Application Manager, DH Systems). These are likely the judges or mentors.
- Grundfos profile: 17M units/yr, USD 5bn revenue (2023), founded 1945 (US since 1973), 20,000 employees, 87.5% owned by the Poul Due Jensen Foundation, 5.4% of revenue reinvested, 65 countries, 15 US sites.
- Demand framing: global mobile traffic 72 EB/month (June 2021) to >220 EB/month (Q2 2026), ">3x in five years" (speaker notes caveat that traffic is not data center energy).
- 373 GW global capacity (71 active, 22 under construction, 280 pipeline), $3T+ investment by 2030 (same as Topic 5). "As much as 98% of the energy used by data centers converts to heat [Alfa Laval]"; "~95-100% becomes heat, up to 85% recoverable".
- Slide 9: "NY leading in the right way: heat reuse" (image only).
- **Four challenge pillars (slide 10): CAPTURE (define the heat source), UPGRADE + DELIVER (select equipment and interfaces), PROTECT RELIABILITY (maintain cooling and heat continuity), CREATE VALUE (quantify benefits and responsibilities).**
- **Site comparison table (slide 11):** 111 8th Ave = urban NYC, existing commissioned multi-tenant DC, dense diverse local demand, focus "match heat supply to users, define upgrades and interfaces", key trade-off "use local demand while protecting data-center cooling reliability". Lake Hawkeye = Lansing NY, former Cayuga Power Plant, proposed DC, nearby homes and community facilities, focus "plan heat pumps and a new network for hot water and space heating", key trade-off "build a feasible network with affordability and community acceptance". "Both sites need justified heat users, dependable delivery and backup heat."

[Analysis] Slide 10's four verbs are a good skeleton for our final presentation; judges from Grundfos and HDR wrote them.

## 3.11 Site profiles: HDR "Regenerative Design Site Data" for both sites (Grundfos Challenge folder)

Both decks share the same 39-page template: regenerative design framing (net positive vs degenerative; KPI categories such as resiliency, campus decarbonization, energy efficiency modeling), then a "Place Profile Review" built from EPA EJScreen, FEMA, WRI water risk, census health data and climate projections. Maps are images; values below are from slide captions and the input panel on page 9. **Neither deck contains any data center engineering data** (IT load, cooling type, temperatures, PUE).

**HDR tool input panel (page 9) [Source]** [Check: several values look like tool defaults or placeholders, e.g. typology "Laboratory", 50 occupants and year of occupation 2030 for an already-commissioned building; do not treat as facility data]

| Field | 111 8th Ave (urban) | Lake Hawkeye (suburban) |
|---|---|---|
| Lat / long | 40.7414, -74.0032 | 42.6025, -76.6334 |
| Overall site area | 110,000 SF | 2,000,000 SF |
| Impervious area excl. buildings | 10,000 SF | 100,000 SF |
| Building footprint | 100,000 SF | 400,000 SF |
| Population density | 102,349 /mi² | 88 /mi² |
| HDR transect | T6 Urban Core | T2 Rural |
| Ecological baseline reference | Rockefeller State Park Reserve, Pleasantville NY | Taughannock Falls State Park, Trumansburg NY |
| Watershed | Lower Hudson | Oswego |

**Place profile comparison [Source]**

| Indicator | 111 8th Ave | Lake Hawkeye |
|---|---|---|
| Biggest biodiversity threat | Urban expansion | Agriculture |
| Noise | 56 dB sustained vs 43.9 baseline | 41.9 dB vs 40.6 baseline |
| Baseline water stress / drought | Low-Medium / Low-Medium | Low-Medium / Low-Medium |
| Groundwater table decline | Medium | Low-Medium |
| Direct discharge to water | 79th pct (runoff to Hudson) | 44th pct (to Cayuga Lake) |
| Impaired waterways | Hudson (IR 5: dioxins, mercury, pesticides, PCBs) | Cayuga Lake and an inlet (phosphorus) |
| Flood | 500-yr floodplain one block away | No apparent risk, FEMA map coverage drops off ("more investigation needed") |
| Precipitation | +5 in within 5 years | +3 in within 10 years |
| FEMA National Risk Index | 1st pct (main hazard hurricane) | 1st pct (main hazard tornado) |
| FEMA Social Vulnerability | 79th pct (less able to avoid disaster) | Population easily able to bounce back |
| Nearby power plants | Two closest are cogen plants at ~654 lb CO2/MWh; one is next to a disadvantaged community | Rates not listed; no disadvantaged communities nearby |
| Future heat | +3 °F by 2050, up to 69 days >90 °F (19 today); +12 °F by 2080 ("feels like Ola, Arkansas") | Same 2050 text; +12 °F by 2080 ("feels like Cherry Hill, VA") |
| AQI days worse than "Good" | 5% (10-yr avg), 10% (5-yr avg): getting worse | 0% and 0% |
| Ozone / PM2.5 | 37th / 52nd pct at site, but 83rd / 92nd pct one block west (HDR suspects diesel backup generators or another combustion source) | 20th / 4th pct |
| Asthma, heart disease, stroke, cancer | Very low / very low / very low / low | 51st / 42nd / 34th pct; cancer high to very high (90th pct) across the lake, in an older population |
| Minority population | 49th pct (block to west 79th) | 24th pct |
| Below poverty | 43rd pct (block to west 83rd) | 28th pct |
| Age 65+ | 42nd pct | 56th pct |

[Analysis] For 111 8th Ave the equity story is the block to the west (higher poverty, minority share and PM2.5), the nearby disadvantaged community next to a cogen plant, and rising summer heat. For Lake Hawkeye the story is a low-density, older, rural population (88 people/mi²), which makes a classic heat network hard to justify on load density and points toward anchor offtakers (greenhouses, community facilities, campus loads) or a small village network. Typo in the deck: the PM2.5 slide for 111 8th Ave says "52nd percentile for Ozone".

## 3.12 Grundfos/Siemens "Connecting data centers and district heating networks" (CBS white paper, May 2023, 22 pp)

**Key arguments [Source]**

- Normal model: DC delivers waste heat to a heating plant owned by a heat supplier working with the network operator. Heat network operators are the preferred project leaders (expertise, regulation, scale); ESCOs a close second (more agile, easier financing).
- Most DC waste heat is at **20-26 °C**; few direct uses (pools, aquaculture), so heat pumps are needed; heat pump COP in reuse typically **3.0-6.0**.
- Heat network generations table: 1G 120-200 °C flow / 100-140 return (steam); 2G 100-120 / 80-110; 3G 80-100 / 60-90; 4G (50) 60-80 / 40-70; 5G 10-25 / 3-15.
- **Three connection options:** (a) Classic: return to feed, ΔT 60 to 80 °C; (b) COP efficient: return to return (preheat return by ~5 °C), 60 to 65 °C; (c) Booster: feed to feed at the network edge, 77 to 82 °C. Can switch seasonally.
- Demand profiles: Helsinki summer demand ~5% of winter; London/Madrid ~20%; Denmark up to 30% (DHW on DH). Networks typically have 30-60% more capacity than peak. A DC can serve the summer DHW base load.
- **Distance:** connection cost rises from 3% to 50% of total capex as distance goes from 50 m to 4,000 m. Heat loss 0.5-1.5% per km in a 70-80 °C system. Upgrading heat at the DH substation (Option B) instead of at the DC cuts losses 3-4x and allows cheaper PE pipe.
- **Assessment chart (Figure 9):** "Great" conditions = fossil heat only; network >20x DC capacity; network temperature <70 °C; distance <100 m; DC >5 MWe; chilled-water cooling; transformation incentives. "Poor" = mostly renewables; network <10x DC; >90 °C; >2 km; <0.5 MWe; evaporative or air free-cooling; no incentives.
- **10 MW use case** (10,000-20,000 households, 100-200 MW network, 1:10 ratio so 100% reuse; electricity €100/MWh; heat pump capex €6M; full 8,760 h): marginal heat cost €19/MWh (COP efficient), €23 (classic), €30 (booster) vs €39/MWh for gas (gas €25/MWh plus €60/tCO2). Classic saves ~€0.5M/yr vs a standalone heat pump on surface water; simple payback ~9 years without subsidy (vs >30 years for an ambient-source heat pump). Up to 70% of capex may attract public funding. DC savings on cooling can exceed €1M/yr.
- Free-cooling conflict: heat is most valuable in winter, exactly when DCs use free cooling. Fix: DC trades its heat for free cooling service (Meta Odense model).
- Ten-year contracts with exit clauses are emerging as standard.

| Table 2 [Source] | Classic | COP efficient | Booster | Standalone HP (surface water) |
|---|---|---|---|---|
| Heating temps | 60-80 °C | 60-65 °C | 77-82 °C | 60-80 °C |
| Heat price €/MWh | 35 | 28 | 40 | 35 |
| COP | 4.5 | 5.5 | 3.5 | 3.5 |
| Heating capacity MW | 12.9 | 12.2 | 14.0 | 14.0 |
| Annual heat MWh | 73,209 | 69,593 | 79,716 | 79,716 |
| Heat revenue €k/yr | 2,562 | 1,949 | 3,189 | 2,790 |
| Electricity €k/yr | 1,709 | 1,329 | 2,393 | 2,393 |

**Checks [Check]**

- Revenue: 73,209 MWh x €35 = €2.56M. Matches.
- Net cash flow: classic 2,562 - 1,709 = €853k; standalone 2,790 - 2,393 = €397k; difference €456k ≈ "€0.5M". Matches.
- Booster net (€796k) > COP-efficient net (€620k) even though booster COP is lower, which supports the paper's point that the most efficient option is not always the most profitable.
- 12.9 MW x 8,760 h = 113,000 MWh, but annual heat is 73,209 MWh, so the "full year, same average load" assumption implies ~65% average load, not full load.
- Payback: €6M / €853k = 7.0 years, not 9. The 9 years presumably includes costs not shown (O&M, connection). Unexplained.
- Implied annual-average heating COP from the table: 73,209 / 17,090 MWh = 4.3 (vs chiller COP 4.5 listed; footnote says COPs are "for chillers only").

[Analysis] This is the most directly reusable techno-economic template in the folder. NYC electricity (~$200-250/MWh per the DATA HEAT appendix) is 2 to 2.5x the €100/MWh assumed, so the European economics do not transfer directly.

## 3.13 Danfoss Impact No. 9, "Waste heat" (~2026, 28 pp)

**Key arguments and numbers [Source]**

- Nearly two-thirds of global energy was wasted as heat in 2024; up to 55% still by 2030. At least 3,100 TWh of waste heat went uncaptured in 2023; recovery could save up to €140bn/yr. EU waste heat ~1,200 TWh (1,517 TWh by 2050). US waste heat 18,028 TWh (2023) vs heating demand 6,389 TWh. China 13,889 TWh (2021), 60% within 10 km of urban areas.
- **Three pathways:** on-site reuse (quickest; payback often <3 years), microgrids/industrial clusters (payback 3-7 years), district heating integration.
- DCs: "nearly zero on-site demand", 24/7/365, ideal for microgrids or DH. US DC consumption expected to quadruple 2023-2030; could supply 33% of US combined residential and commercial heating demand. IEA: DC heat could cover up to 10% of Europe's space-heating demand by 2030.
- Temperature mismatch: waste heat 30-60 °C vs DH 70-100 °C. Denmark lowered networks from ~100 °C to ~70 °C, giving heat pump paybacks of ≤5 years vs 10+ years in Germany (networks near 100 °C).
- **Barrier:** unfavorable electricity-to-gas price ratio; heat pumps need cheap electricity relative to gas.
- **Cases:** Hydro Tønder aluminum plant (heat pump 16 °C to 60 °C, COP 4.9; booster to 90 °C, COP 3.8; 205,600 m³ gas/yr and 407 t CO2/yr avoided; 2.3-year payback). Wuqing Qingshu Science Park, Tianjin (103,450 m² complex ~400 m from two DCs; winter space heating plus year-round DHW, summer switches to cooling; heat cost ~60% below local commercial DH in first winter; 1.1 GWh/yr energy and 1,659 t CO2/yr saved; payback <3 years). Southern Denmark University AI supercomputer designed to feed local DH.
- **German analysis:** 178 DH networks (>5,000 households each), emitters ≤500 °C within 1 km (QGIS): waste heat covers ~30.4% of their demand, above the 30% legal 2030 threshold, even excluding DCs (>3,000 German DCs, ~1,000 in Energy Efficiency Act scope). Limits: declared not verified data; static snapshot, no seasonal or hourly matching.
- Recommended actions for operators: lower network temperatures, map and publish waste heat, flexible tariffs, long-term heat purchase agreements, protect heat corridors. For industry: continuous real-time metering of waste heat.

[Analysis] The German GIS method (buffer zone + supply/demand ratio per network) is a simple, defensible geospatial screening approach we could replicate for NYC or Tompkins County, and the paper itself flags its main weakness: no temporal matching. That gap is exactly what the brief asks for.

## 3.14 Danfoss Impact No. 3, "Roadmap for decarbonizing cities" (2023)

Mostly about buildings, transport and ports; data-center-relevant parts only. [Source]

- Buildings: thermostatic radiator valves save up to 7% (1-year payback); hydronic balancing up to 10%; model predictive controls up to 20% of energy cost (London case: payback in 11 months, 600 MWh heat saved); heat pumps use ~1/3 the electricity of resistance heating.
- District cooling uses about half the energy of air conditioners; can be >2x as efficient as decentralized systems.
- **AWS Dublin (Tallaght):** DC heat for 47,000 m² of public buildings, 3,000 m² commercial and 135 affordable apartments; ~1,500 t CO2/yr.
- Frankfurt estimate: DC waste heat could cover all residential and office heat demand by 2030.
- IEA: DCs used 220-320 TWh in 2021 (~1% of global electricity).
- Supermarket SuperBrugsen (Denmark): 78% of its heat from refrigeration heat recovery since 2019; sold 134 MWh to the local DH grid.
- Wastewater: Marselisborg WWTP (Aarhus) produces ~100% more energy than it uses; 4.8-year return.
- Excess heat from accessible urban sources could cover 10% of EU total energy demand.

## 3.15 Grundfos "Every Drop Counts" water scarcity paper (2026)

Mostly US water efficiency policy. DC-relevant points [Source]:

- ~60% of US land and half the population face medium-to-high water stress in a typical year.
- Thermoelectric power cooling = ~40% of US water withdrawals; power plants use ~12,000 gal/MWh (withdrawal basis).
- DC direct draw is <1% of US water; the larger share is indirect through electricity.
- An evaporatively cooled DC can use 18,000-550,000 gal/day (60-1,800 households); a closed-loop DC of similar scale uses almost no water after the initial fill. Operators have invested nearly $800M in utility water partnerships.
- Water-energy nexus: a cooling system that uses no water often uses more energy, shifting water draw to the power plant.
- Industrial "measure, reduce, reuse, reclaim" can cut freshwater intake 75-90% (Intel Chandler: 98% recovered).

[Analysis] Relevant to Lake Hawkeye, which uses closed-loop glycol cooling (low water), and to any claim that heat reuse "saves water": the saving is real only where the DC would otherwise use evaporative towers (likely more relevant at 111 8th Ave).

## 3.16 Resource Innovation Institute, "Colocating Data Centers & Greenhouses" (Virginia, June 2025, 54 pp)

**Key findings [Source]**

- Colocating one DC with one greenhouse is technically feasible but **not functional** because of heat-load mismatch: "If you put a 10-hectare greenhouse next to it, then we need 10 megawatts. They have 50." Greenhouse demand varies diurnally and seasonally; DC load is flat.
- DCs pursue colocation mainly for public image and community acceptance, not economics. They demand "five nines" uptime and reject anything that risks reliability or construction timelines ("stay out of my way"). Recommended: build the DC first as "CEA-ready" with an intermediary substation (heat exchangers and meters), never shared fluids or joined buildings; heat exchange substations up to 0.6 miles away.
- Optimal model: an integrated **Farm Park** with a Central Resource Hub (heating water, chilled water, CO2, compressed air, power, fiber), a CHP (gas or biogas) that cools the DC loop and supplies greenhouses with power, heat and CO2. Multiple greenhouses plus packaging, distribution, digesters, breweries etc. smooth the demand. Note that DC heat alone provides no CO2 enrichment for greenhouses.
- Waste heat temperatures (Table 1): legacy air-cooled 30-40 °C (not suitable); standard water-cooled 45-55 °C; AI/HPC liquid 55-70 °C; two-phase up to 90 °C. Greenhouses need ~75 °C on the coldest days.
- Virginia's DCs (~3.4 GW) could support 6,000-8,500 acres of greenhouses, 80-120% of state tomato demand, offsetting 370-495 million m³ of gas/yr.
- Each 65-acre greenhouse creates 140-270 jobs. Average tax per acre in six Southern Virginia counties: farmland $3.53, greenhouse $4.44, DC $609.
- **Agriport A7 (Middenmeer, NL):** 630 ha greenhouses, 75 ha DCs; 7 growers; >50 CHP units (>200 MWe); heat mix CHP 71%, geothermal 17%, biomass 8%, boiler 4%; 2,400 greenhouse jobs, 1,500-2,000 DC jobs. Netherlands bans DCs >10 ha and 70 MVA in zoning plans; Noord-Holland requires a waste heat economic analysis at permit stage.

**Checks and weak points [Check]**

- "Modern data centers convert 33-42% of consumed power into waste heat" contradicts physics and every other source in the folder (95-100%). Likely a misreading of the recoverable or usable share. Do not cite.
- 10 MW per 10 ha implies ~1 MW/ha peak greenhouse heat, consistent with Dutch glasshouse norms. [Unverified]

[Analysis] Directly relevant to Lake Hawkeye: rural, agricultural, near Cayuga Lake. A single greenhouse cannot absorb a 150-300 MW site; a cluster or park model plus storage is the only credible greenhouse story. The CHP-based Farm Park conflicts with decarbonization goals unless biogas-fired.

## 3.17 DATA HEAT: "Sector Coupling of Data Centers & District Heating" (Reshape Strategies for NYSERDA, IDEA and the Danish Trade Council, Feb/Mar 2026, 159 pp)

The most policy-relevant document for New York. Funded partly by NYSERDA.

**Technical [Source]**

- Five configurations (same as Topic 5, with real examples): **Ambient** (Amazon Eco-District, Seattle), **Hybrid ambient/centralized** (Meta and Fjernvarme Fyn, Odense), **Centralized** (Microsoft and Fortum, Kirkkonummi, Finland), **Chip heating** (First Block/Heat Connect, Quebec; T Loop, Sweden exploring), **Indirect via district chilled water** (Enwave Toronto; Stockholm Data Parks). Temperature bands: full-service heat 50-90 °C, low-temperature waste heat 15-40 °C, cooling service 5-25 °C.
- DC heat beats other heat pump sources (air, surface water, wastewater, solar) on both **temperature** and **density** (heat per unit area accessed), which matters in space-constrained cities.
- Thermal storage: daily tanks decouple supply and demand and add resilience if DC heat drops; seasonal borehole storage can absorb summer surplus for winter, but only "if the fundamental economics are sound to begin with".

**Business [Source]**

- Stakeholders: DC (cares about time to market, reliability, low opex), DE utility (financial return), building (low-cost, low-carbon heat).
- Thermal equipment is a small share of DC capex: avoided capex from heat reuse "in the order of <<5%" (appendix says thermal equipment can be <2-3% of total capex). OPEX savings high bookend <25%, realistic <5% (EU average operational heat reuse ~15%).
- Conclusion: for DCs the benefits are small relative to perceived risks to schedule and uptime; without policy, only opportunistic projects happen. For DE utilities and buildings, DC heat can be very attractive. Any payment to the DC for heat raises the building's heat price.
- Social license: interviewees said heat recovery can improve local acceptance of DCs more than tax revenue or remote renewable purchases.

**Policy framework [Source]**

- Indirect: green building standards, energy planning, DE policies. Targeted: awareness and pilots, mapping and reporting, zoning (DC zones near heat demand), study requirement, heat-reuse-ready requirement, heat-reuse provision (free heat when a network exists), direct legislation (e.g., % of IT load), tradeable heat reuse credits (remote hyperscale DCs buy credits from urban edge DCs), taxes on rejected heat, tax credits, funding, property tax tools (PACE), electric utility rates and interconnection priority, insurance pools for heat supply risk.
- Germany's Energy Efficiency Act: new DCs 10% reuse (2026), 15% (2027), 20% (2028), with feasibility exemptions; some pressure to remove.
- Norway: 9 of the 18 largest DCs have heat recovery despite few DE networks.
- **Most favorable segment:** new HPC (liquid-cooled) edge DCs (<50 MW) near existing hot-water DE networks; also new edge DCs near high-density new construction, or near steam DE (boiler feedwater preheat, future hot-water conversion). Hyperscale (>50 MW, far from DE) is least favorable.

**New York specifics [Source]**

- NY DC market: "growth has slowed"; under-construction pipeline 40 MW, planned 186 MW; >50% of new capacity is expansion of existing facilities; power and land constrained.
- NYC: ~2,600 HDD (base 18 °C), climate zone 4A, 12.7 °C mean, 11,300 people/km².
- **Con Edison steam:** largest district steam system in North America, >1,700 Manhattan buildings, parts from the late 19th century. "Steam systems are not compatible with data center heat recovery without a steam to hot water conversion."
- UTENJA (2022, S9422) lets utilities own and operate thermal networks; 13 TEN pilots proposed in 2023, one withdrawn; DPS approved 10 for engineering and design by 2024. NY HEAT Act (S4158) introduced Feb 2025. "2022 TEN law and NYSERDA pilots explicitly support waste heat reuse; Local Law 97 allows TEN offsets." NYS all-electric code for large new construction; LL97 requires ~40% GHG cut by 2030.
- **NYC large-load electricity (Con Ed SC-9): ~$200-250/MWh blended** (supply ~$90 + delivery ~$130). NY grid emission factor listed as **442 kg CO2e/MWh**, falling with 70% renewables by 2030. [Check] 442 kg/MWh looks high for the NYS average and may be a NYC/marginal figure; verify against NYISO/EPA eGRID before use.
- Pending: Sustainable Data Centers Act (S.6394): clean energy targets for large DCs (33% by 2030, 100% by 2050). NYSERDA DC efficiency incentives up to $5M/project. PSC Case 23-E-0434 on large flexible loads.
- "There are no regulations today that directly require heat re-use from data centres" in any of the six jurisdictions studied (AB, ON, QC, CA, NY, VA).
- Opportunity ranking: **New York is a "Top Tier" market** (strong building decarbonization policy, emerging TEN market) with the con that most DCs are existing.
- Community backlash: $64B of US DC projects blocked ($18B) or delayed ($46B) in two years; 142 opposition groups in 24 states.
- San José "Net Zero Community" (Westbank and PG&E): three DCs plus up to 4,000 homes on a TEN, first DC online late 2027.

[Analysis] Two direct implications. (1) For 111 8th Ave, the network next door is Con Ed steam, which cannot take low-grade heat; the realistic urban options are building-level hydronic customers, a new ambient TEN, or steam-condensate/feedwater preheat. (2) The report's argument that DCs gain little financially means our ownership model should put the heat pump and network capex on a utility/TEN operator or ESCO, not the DC.

## 3.18 driving_sustainable_data_centres (IQ-EQ, Norton Rose Fulbright, ULI, BuildingMinds; July 2025; "AD Highlighted")

ESG and investor-focused. Heat-reuse-relevant points [Source]:

- **German Energy Efficiency Act (in force end of 2023):** new DCs starting operation from 1 July 2026 must use at least 10% reused energy, 15% from 1 July 2027, 20% from 1 July 2028; all DCs must avoid or reduce waste heat per state of the art. [This confirms the open question from 3.8.]
- Claim: "While there are currently no national thermal output reuse requirements in the United States, California has required waste heat recapture for data centres under the 2022 Building Efficiency Standards (Title 24)." [Unverified: check the actual Title 24 provision; DATA HEAT says no jurisdiction it studied, including California, directly requires DC heat reuse.]
- ~40% of a DC's power goes to traditional cooling (claim, varies widely); mid-sized DC uses ~300,000 gal/day of water (NPR); 1 MW DC ~25.5 million L/yr (WEF).
- Nordic DCs feed DH; heat recycling can be "a competitive advantage in securing planning approvals and investment".
- Brownfield power plant sites suit DCs because they have large grid connections and sometimes DH access. [Analysis] This is the Lake Hawkeye situation (former Cayuga coal plant).

## 3.19 IDEA "Thermal Energy Storage for Data Centers" (CB&I, New York State folder)

**Content [Source]**

- DCs are mission-critical: redundancy, high cooling capex/opex, and heat rejection that may not match variable demand. Cool TES gives emergency backup and peak shaving; **hot TES can balance heat rejection with heat demand**.
- Installed costs: TES $200-500/kWh (large chilled-water TES); Li-ion $500/kWh; pumped hydro $611/kWh; CAES $244/kWh; flywheels $11,520/kWh.
- TES vs batteries: round-trip efficiency near 100% vs ~68-86%; life 40+ years vs 3-15; no fire or toxic disposal risk.
- Cases: State Farm Bloomington (2 x 44,800 ton-hr tanks, 4 million gal each; shifts 13,000 tons and ~10 MW peak). DC operators with chilled-water TES include Google (37,667 ton-hr at 4 sites), DuPont Fabros, Microsoft, Equinix. **Princeton University:** four TES types including 1,000 ton-hr for DC emergency cooling (30 min ride-through), 421 million Btu hot water TES and 19,680 ton-hr CHW TES to balance geo-exchange; peak cut 10,000 tons / 7 MW for 4 h/day; **geo-bores reduced from 3,100 to 2,100, saving $25M net capex.**
- ERCOT example: at a ~70,000 MW peak, ~23,000 MW of installed wind produced <600 MW.

**Checks [Check]**: 421 million Btu = 123 MWh thermal. 44,800 ton-hr x 3.517 kWh/ton-hr = 158 MWh cooling. The $/kWh figures for TES are per kWh of thermal capacity, while battery figures are per kWh electric, so the comparison is not like-for-like (TES $/kWh thermal must be divided by the chiller/heat pump COP to compare). Vendor presentation; cost figures undated.

[Analysis] Storage protects both directions of reliability the brief asks about: CHW TES gives the DC cooling ride-through, hot water TES covers heat customers if DC heat drops, and storage reduces heat pump and borefield sizing (Princeton saved $25M).

## 3.20 June 10, 2026 FPCJ meeting summary and urbs feasibility study (First Presbyterian Church in Jamaica, Queens; New York State folder)

The only New York data-center-adjacent heat reuse feasibility study in the folder.

**Context [Source]**

- FPCJ's 100-year-old Magill Building (built 1925, 3 stories, 26,000 SF) sits next to a **Verizon switchgear and data facility** whose dry coolers reject heat just beyond the church property line. NYSERDA funded urbs (Urban Systems) to study capturing it. Workshop convened by FPCJ and Metro IAF Clean Energy Initiative, with Verizon, NYSERDA, NYC EDC, Danfoss, Alfa Laval, Endurant and the Swedish Consulate.
- Church problem: high energy costs and a failing VRF system with refrigerant leaks; already disconnected from gas.
- Verizon's concerns: not a traditional DC; multi-generational equipment in many rooms, each cooled separately, rejecting via **individual dry coolers, not a central loop**; long-term plan for the facility uncertain; insisted on **redundancy so the church does not depend solely on Verizon heat**; as a for-profit, needs to understand cost-benefit. NYC EDC offered to help with regulatory issues of **transferring heat from one property to another**.

**Numbers [Source]** (currency symbols did not extract; values assumed to be $)

- Baseline: energy model 778 MMBtu vs utility bills 829 MMBtu (6% deviation); EUI 26 kBtu/ft²; 66 tCO2e/yr; ~$75,296/yr energy cost; space heating is the largest end use.
- Five analyzed dry coolers, ~60 tons each, reject an estimated **16,070 MMBtu/yr**; the site has an estimated 25-35 dry coolers in total.
- Magill heating demand ~441 MMBtu/yr; only **~343 MMBtu/yr of recovered heat (~2% of the five coolers' rejection)** is needed with heat pumps.
- Concept: capture from Verizon's dry cooler glycol loops, intermediary energy transfer station (est. $300,000-400,000), heat pumps (est. $300,000-400,000), low-temperature hydronic ambient loop in the church; keep VRF for cooling.
- Impact: 60-100% of heating from recovered heat; HVAC energy 441 to 297 MMBtu (-33%); HVAC GHG 37 to 25 tCO2e (-33%); total building energy -18%; annual cost ~$75,296 to ~$61,418.
- Next steps: low-temperature hydronic system design; more data on Verizon's heat; schematic design; cost/financing and institutional barriers; fact-finding on technical, institutional and regulatory solutions.

**Checks [Check]**

- Implied heat pump COP: 441 delivered / (441 - 343) electricity = **4.5**. Plausible for a low lift from glycol.
- Capacity: 5 x 60 tons = 300 tons ≈ 1,055 kW cooling. At full load all year that is ~31,500 MMBtu; 16,070 MMBtu implies ~51% average load factor (rejected heat also includes compressor work, so the IT-side load is lower). Reasonable "conservative" assumption.
- Savings: $75,296 - $61,418 = $13,878/yr. Against $600,000-800,000 capex that is a **simple payback of ~43-58 years** before incentives. The summary does not state a payback; this is the weak point of the project economics. [Analysis]
- 33% HVAC reduction: 297/441 = 0.67. Matches.

[Analysis] This is a near-perfect analogue for 111 8th Ave on the institutional side: a multi-tenant/legacy telecom facility, distributed dry coolers, an operator who will not guarantee supply, a neighbor needing a hydronic retrofit first, and property-line heat transfer as an unresolved regulatory question. It also shows that a single small building uses a tiny fraction of available heat, so offtaker aggregation matters.

## 3.21 urbs "Williams College Energy Transition Strategy" v1.0 (Dec 2022) and the Williams College audio transcript

**Document [Source]**

- Williams College (Massachusetts) baseline: natural gas 151,789 MMBtu; electricity 107,552 MMBtu; heating 155,988 MMBtu (peak 99,262 MBH, 10,210 tCO2e); cooling 51,249 MMBtu (peak 38,390 MBH, 1,669 tCO2e). Heating 57% of energy, cooling 19%; heating and cooling together 85% of GHG. Summer cooling peak ~1/3 of winter heating peak.
- **Energy flow:** 196,875 MMBtu in, 155,988 MMBtu of heat produced, **98,437 MMBtu delivered (50% loss in combustion and distribution)**. Rejected heat that could be captured: **66,624 MMBtu condenser heat** from chillers via cooling towers and **19,687 MMBtu** from exhaust ventilation.
- Strategy: replace central gas/steam with decentralized "energy nodes" that balance simultaneous heating and cooling (5th-generation DE thinking). Size new infrastructure to capture waste, not to replace 1:1.
- **Node 1:** 8 science/lab buildings (Clark Hall, Wachenheim, Thompson Biology/Chemistry/Physics labs, Morley, Hopper, Jesup, Morgan, West College) = 25% of campus energy and 23% of GHG; highest heat rejection and most balanced cluster.
- Node 1 design: existing chiller plant becomes the energy center, boosted by a water-source heat pump; **120-150 boreholes ~800 ft deep** store summer condenser heat as seasonal storage, used when average temperatures drop below 32 °F; **dry coolers + heat pump** cover heating above 32 °F and can top up the boreholes after cool summers; **thermal storage tank sized for 4-6 hours of peak heating**; new AHUs with heat recovery; point-of-use electric heat for extreme peaks; some gas retained for right-sizing.
- Node 1 heat supply (chart): 19,436 MMBtu from condenser waste heat via boreholes; 17,492 MMBtu ground-source heat pumps; 8,292 MMBtu air-source heat pumps; 6,858 MMBtu reduction from ventilation recovery; 1,646 MMBtu point-of-use electric.
- Node 1 impact: primary heating energy 34,288 to 9,563 MMBtu (-72%); heating GHG 2,275 to 311 tCO2e (-86%); peak input 17,001 to 6,800 MBH (-60%). Campus-wide: heating primary energy 155,988 to 50,367 MMBtu (-68%), cooling 51,249 to 23,447 (-54%), heating GHG 10,210 to 1,640 tCO2 (-84%), cooling GHG 1,669 to 764 (-54%).
- Targets: Williams 80% Scope 1 cut by 2035; Massachusetts building emissions -28% by 2025 and -47% by 2030 (vs 1990); electric power emissions -53% by 2025 and -70% by 2030. Node 1 framed as a "living lab".

**Checks [Check]**: 98,437 / 196,875 = 50.0%. 9,563 / 34,288 = -72.1%. 311 / 2,275 = -86.3%. 6,800 / 17,001 = -60.0%. 50,367 / 155,988 = -67.7%. 1,640 / 10,210 = -83.9%. All reported percentages reproduce.

**Audio transcript (18.8 min, uploaded Oct 3) [Source, secondary]**: an AI-style two-host "deep dive" podcast summarizing the urbs document. It reproduces the document's numbers correctly with these differences:

- It says heating alone causes 85% of GHG; the document says 85% is from heating **and** cooling. [Check] Use the document.
- It adds unsourced details not in the document: borehole fluid "maybe 50 or 60 °F", antifreeze in the loop, plate heat exchanger mechanics, and resilience claims that thermal tanks let the node "completely decouple from the grid" during a blackout. The document only says storage covers 4-6 hours of peak heating and that electrification protects against market volatility. Treat the podcast's resilience framing as interpretation, not source.
- It closes by explicitly naming urban data center exhaust and subway heat as untapped sources for neighborhoods, which is a useful framing line but not evidence.

[Analysis] The transferable pattern for our challenge: capture condenser heat in summer, store it seasonally in boreholes, use heat pumps in winter, add short-term tanks for peaks, and keep a small backup. This directly answers the brief's seasonality and continuity criteria. The urbs team also authored the FPCJ study, so this is likely the approach the New York State materials are pointing toward.

## 3.22 NYSERDA "Resource Efficient Decarbonization" (Empire Building Challenge, New York State folder)

**Framework [Source]**

- RED model: **Reduce** loads, **Reconfigure** to thermal networks and low-temperature distribution, **Recover** heat (waterside, airside, wastewater), **Replace** equipment incrementally. "All-or-nothing is a false assumption."
- "Steam is out. Water is in." Shift steam to hydronic; embrace low-temperature heating (fan coils, radiant panels) to enable heat pumps; choose technology-neutral distribution.
- Business case: NPV vs business-as-usual including LL97 fines, avoided equipment replacement and façade (LL11) costs; find the lowest marginal cost of decarbonization.
- **Empire Building Challenge:** $50M for technical assistance and implementation; **$10M Empire Technology Prize** [this is almost certainly the "Empire Tech" heat pump category in the HDR temperature chart, i.e. NYSERDA-backed higher-temperature heat pumps; resolves open question 4]. 16 NY portfolio partners (10 commercial, 6 multifamily), 228M ft², 70K housing units; public commitments to decarbonize >125M ft².

**Demonstration projects [Source]**

| Project | Size | Key heat recovery measure | Baseline to target | NYSERDA / private $ |
|---|---|---|---|---|
| Whitney Young Manor, Yonkers (affordable) | 230,000 SF, 195 apts | Hydronic loop, central ASHP, **wastewater energy transfer (18,000 gal tank, SHARC heat pumps)**, gas backup | 96 to 48 kBtu/SF; 1,456 to 273 tCO2e (-81%) by 2035 | $5M / $12M |
| The Heritage, East Harlem (mixed income) | 680,000 SF, 600 apts | PTHPs, CO2 heat pump DHW, ERV | 77 to 45 kBtu/SF; 3,414 to 1,072 tCO2e (-69%); avoids $34,424/yr LL97 fines | $5M / $14M |
| The Towers, Bronx (co-op) | 425,000 SF, 316 apts | Steam to hydronic, wastewater heat recovery, geothermal | 111.6 to 32.5 kBtu/SF; 2,771 to 202 tCO2e (-93%) | $3M / $16.6M (roadmap $27M) |
| Empire State Building | 2.85M SF | WSHPs on condenser water loop, ERVs (district steam today) | 84 to 50 kBtu/SF; 15,640 to 3,986 tCO2e (-75%) | $5M / $40M+ |
| **345 Hudson St (Hudson Square)** | 857,000 GSF | **Converts condenser water riser to an ambient loop** for heat sharing; WSHPs (Energy Machines); "Nordic design principles" | 75 to 38 kBtu/SF; 4,999 to 1,500 tCO2e (-70%); avoids $204,000/yr LL97 | $5M / $30M+ |
| 601 Lexington | 1.5M SF | Heat recovery to cut steam | 86.3 to 73.6 kBtu/SF; 3,920 to 2,899 tCO2e (-26%) | |
| 660 Fifth Ave | 1.4M SF | WSHPs; connect retail/tenant supplemental cooling loops to main condenser loop; 120-130 °F heating water | 119.5 to 47.9 kBtu/SF; 12,508 to 3,059 tCO2e (-76%); avoids $340,000/yr LL97 | $3M / $6.7M |
| LeFrak City Plaza, Queens | 396,000 SF | Heat recovery chillers; core/perimeter split; future campus TEN connection | 103.5 to 51.3 kBtu/SF; 3,330 to 358 tCO2e (-89%) | |
| 520 Madison | 1.0M SF | Condenser heat recovery, **UrbanGeo geothermal under the building**, ice heating, thermal layering | 87.4 to 28 kBtu/SF; 2,294 to 1,166 tCO2e (-49%) | $3M / $22.2M |
| PENN 1 | 2.5M SF | Condenser water heat recovery; **convert CRAC units from DX to chilled water to maximize heat recovery**; thermal dispatch; retire cogen; keep steam as backup | 167 to 49 kBtu/SF; 18,750 to 1,638 tCO2e (-91%); avoids $790,000/yr LL97 | $1M / $3M (one measure) |

[Analysis] This is the demand side for an urban proposal. Large Manhattan buildings are already being re-plumbed to low-temperature hydronic loops with water-source heat pumps on condenser loops, which is exactly the interface DC heat needs. 345 Hudson St (Hudson Square, south of the 111 8th Ave site) is converting to an ambient loop. LL97 fines give a dollar value for avoided emissions. The PENN 1 CRAC conversion shows even server rooms in office towers become heat sources once moved to chilled water.

## 3.23 US Policy Landscape, Data Center Heat Reuse (David Gardiner & Associates, 8 slides)

**Content [Source]**

- Policy options. Enabling: demonstration projects; matching platforms between DCs and heat users; co-location planning; district thermal networks. Incentives: tax credits; grants or low-interest loans; prioritized permitting or interconnection for DCs that reuse heat. Standards: efficiency standards that count heat reuse; require heat reuse plans in permitting of new DCs; fee on DC electricity emissions.
- 2026 activity: Virginia passed a law directing a state study of DC heat reuse; Illinois POWER Act could include heat reuse; California bill to let utilities operate TENs (some opposition).
- US projects: Syracuse University (DC heat to adjacent office), Notre Dame (DC heat to greenhouse), Westbank San José (DC heat to 4,000-unit residential district system); Europe: Microsoft greenhouse warming, Amsterdam.

## 3.24 CenTrio / Thornton Tomasetti, "Developing Community and Data Center Synergies with District Energy"

**Content [Source]**

- 25+ US DC projects cancelled due to community backlash; concerns: utility costs, water, stewardship, resistance to AI. Communities no longer accept tax revenue, land monetization and jobs as sufficient justification.
- **Metropolis Pointe, Bronzeville (Chicago):** mixed-use development with a DC, residential tower, retail and an AI-preparedness institute. A district plant cools the DC and captures its heat for the rest of the development. The DC revenue makes the whole development investable (prior attempts on the site failed). Status: talks with offtakers, community meetings, alderman support.
- **Integration approach (design rules):** maximize server exit temperature without compromising chips; let the compressor add temperature lift for higher-enthalpy heat; DHW needs high temperature but small quantities; secondary heating uses lower temperature but larger quantities (cascade); aim for the lowest possible temperature before the cooling tower or fin-fan loop; choose ΔT per system to maximize cooling efficiency and PUE; max system size is limited by how much heat the buildings can absorb.
- Challenges: shifting technical scope (offtaker-dependent), DC tenants must accept non-traditional cooling, new financial and risk structures, community education.

[Analysis] The temperature cascade (DHW first, then space heating, then lowest-grade uses, then rejection) is a clean design principle for our supply/demand matching.

## 3.25 iMasons podcast transcript (project file; auto-generated captions, some numbers garbled)

**Content [Source]** (David G., independent consultant, OCP heat reuse workstream)

- Most heat reuse projects are in Europe because the energy crisis made heat valuable.
- **Municipal swimming pool case:** instead of three 900 kW gas boilers, a 100 kW DC heat source halved gas use; but pool demand falls in summer, so a dry cooler was added to keep IT load constant. Even pools are "not a perfect match"; a heat sink that takes energy regardless of season is better.
- Hot climates: couple DCs with thermal desalination; ~5,000 m³/day of seawater can cool 10 MW of IT while the DC preheats the water, lowering fresh water cost.
- Liquid cooling: rack density ~100 kW vs 15 kW conventional; no raised floor or hot/cold aisles (~20x less space claimed); facility water ~20 °C for air vs ~40 °C for liquid; server fans can be up to 35% of rack power in new GPU servers; example facility drops from ~3 MW to ~1.8 MW total input for the same compute, i.e. ~40% more IT capacity under the same grid limit. [Check: transcript is garbled here ("126 instead of 130 racks"); treat as illustrative]
- Temperatures: air-cooled rear-door HX ~34 °C in / 44 °C out; on-chip liquid up to ~70 °C out (the caption reads "7 °"), which can meet DH temperatures without a heat pump. Higher grade heat is much easier to get paid for.
- **Main barriers:** legal departments and guarantees (each party wants independence); and capacity mismatch, e.g. a 300 MW greenfield DC whose nearest users are villages needing ~500 kW. "It's very important to match the heat use in the surroundings and build the data center according to that need." Easy win: small in-building server rooms (~500 kW) piped to the same building's heating.
- Software and hardware utilization (some servers ~5% utilized) can cut IT load far more than cooling efficiency; warns against greenwashing.

[Analysis] The 300 MW vs 500 kW village example is effectively the Lake Hawkeye problem stated by an industry practitioner.

## 3.26 Cross-cutting findings after all documents

### New or strengthened constraints

1. **The DC has little financial reason to participate** (DATA HEAT: avoided capex <<5%, opex <5%; FPCJ: Verizon needs a cost-benefit case). Our ownership model should put network and heat pump capex on a TEN operator, utility or ESCO, give the DC zero-risk terms (no cooling dependency, free or cheap cooling service, social license), and possibly pay for heat later.
2. **Offtaker capacity is the binding constraint at large sites** (RII 50 MW vs 10 MW; iMasons 300 MW vs 500 kW; FPCJ uses 2% of five coolers). Aggregation, storage and clustering are required.
3. **Seasonal mismatch has a proven answer: borehole seasonal storage plus heat pumps plus short-term tanks** (Williams College, Princeton, DATA HEAT appendix, Grundfos Bjerringbro aquifer).
4. **Manhattan's network is steam** (Con Ed, >1,700 buildings) and cannot take DC heat without conversion; but NYSERDA's Empire Building Challenge shows large buildings are converting to low-temperature hydronic loops with WSHPs on condenser loops, which creates new hydronic offtakers.
5. **Economics in NYC are harder than in Europe:** electricity ~$200-250/MWh vs €100/MWh in the Grundfos/Siemens case. Value must also count LL97 fine avoidance, avoided equipment and grid/peak benefits.
6. **No direct DC heat reuse mandate exists in New York** (or any North American jurisdiction studied); Germany's 10/15/20% rule is the reference. NY has UTENJA TEN pilots, LL97, all-electric new construction code, and a pending Sustainable Data Centers Act.

### Contradictions added

| Topic | Values | Sources |
|---|---|---|
| Share of DC power that becomes heat | 33-42% vs 95-100% | RII (likely error) vs all others |
| Typical DC waste heat temperature | 20-26 °C vs 30-40 °C (legacy air) vs 45-55 °C (water-cooled) | Grundfos/Siemens vs RII |
| Payback | ~9 yrs (Grundfos/Siemens 10 MW, table implies ~7) vs <3 yrs (Danfoss cases) vs ~43-58 yrs implied (FPCJ, before incentives) | Various |
| Avoided DC capex | <<5% vs <2-3% | DATA HEAT main report vs appendix |
| US heat reuse mandate | "California requires DC waste heat recapture (Title 24)" vs "no jurisdiction requires it" | Driving Sustainable DCs vs DATA HEAT |
| Williams GHG share | 85% from heating vs 85% from heating and cooling | Podcast vs urbs document |

### Open questions resolved

- Germany 10-20% reuse requirement: **confirmed** (Energy Efficiency Act: 10% from July 2026, 15% July 2027, 20% July 2028 for new DCs).
- NY TEN law: **UTENJA (2022)** applies; 10 utility TEN pilots in engineering and design.
- "Empire Tech" heat pumps: tied to **NYSERDA's Empire Building Challenge / $10M Empire Technology Prize**.
- Manhattan steam: **confirmed** incompatible with low-grade DC heat without steam-to-hot-water conversion.
- NYC electricity price and grid factor: **DATA HEAT gives ~$200-250/MWh (Con Ed SC-9) and 442 kg CO2e/MWh** (factor needs verification).
- Storage cost: **TES $200-500/kWh thermal** (CB&I, vendor). Heat pump capex: **~€6M for 10 MW cooling** (Grundfos/Siemens, Europe) and **$300-400k each for a heat pump and an energy transfer station at ~100 kW scale** (FPCJ).
- Williams College audio: **reviewed via transcript.**

### Still open

1. Site engineering data for both sites (IT load, cooling type, supply/return temperatures, PUE). Still missing from every document.
2. Who the actual tenants and cooling plants are at 111 8th Ave, and whether it is the heat source in Con Ed's Chelsea TEN pilot.
3. Verify the NY grid emission factor and the California Title 24 claim.
4. Ask organizers for the promised GIS/data-source list, community impacts presentation and terminology guide.
5. Heat demand data for candidate offtakers near each site (e.g., NYC LL84 benchmarking data for Chelsea buildings; Lansing schools, NYSEG territory, greenhouses near Cayuga Lake).

---

