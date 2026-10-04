# Slide numbers: check against the current model

Computed on 2026-10-04 from the current code (`heatsim/`, same code path as `app.py`) at the app's
**default settings**, unless a row says otherwise:

- 1.5 MW capture, 1.0 MW average demand (source side), hot water only (0% space heat)
- 12 MWh PCM, 2.5 MW charge/discharge, condenser-water placement, 84 F melt
- 200 h/yr data center outages, "No reserve" policy
- $15/MMBtu NYCHA price, $120/kWh storage, $6,000/ft pipe, $0.25/kWh electricity, $40/MMBtu steam
- No commercial sales, no utility cost recovery, floor-space credit **off**

Demand and weather are **SYNTHETIC** profiles calibrated to the brief. They are not metered data.
Every result below inherits that. "ASSUMPTION" marks an input that is our own assumption, not a cited figure.

**Status key:** **Holds** = the old deck value matches the model after rounding. **Update** = the old
value is wrong and the slide needs the new number. **Not from model** = our code does not compute it.

## Deck claims

| # | Deck claim (old value) | Current value | How it is computed | Status |
|---|---|---|---|---|
| 1 | NYCHA hot water cost $32 vs steam $40/MMBtu (-20%) | **$32.14 vs $40.00/MMBtu (-19.7%, shown as -20%)** | `finance.customer`: heat pump electricity 293.071 kWh/MMBtu ÷ COP 3.4 × $0.25 = $21.55, plus network charge $15 × (3.4-1)/3.4 = $10.59. Steam $40 is the Con Ed bill example, treating 1 Mlb ≈ 1 MMBtu (ASSUMPTION). $0.25/kWh is a working assumption (ASSUMPTION). | Holds |
| 2a | Storage installed cost $1.80M | **$1.80M** | 12 MWh × $120/kWh × 1.25 (25% soft costs) | Holds |
| 2b | Tax credit -$0.54M | **-$0.54M** | 30% ITC × $1.80M | Holds |
| 2c | Net storage cost $1.26M | **$1.26M** | $1.80M - $0.54M (`finance.storage_value`, "Storage capex" metric on the Storage tab) | Holds |
| 3 | Floor space saved vs water tank $160K/yr | **$60K/yr** (condenser side, floor credit on) | (condenser-side tank 2,987 sq ft - PCM 847 sq ft) = 2,140 sq ft × $28/sq ft. $28/sq ft is our pick of one-third of Midtown South asking rent (ASSUMPTION). Condenser-side tank swing is 87 to 65 F (ASSUMPTION). The old $160K is the **loop-side** tank: (6,572 - 847) sq ft × $28 = $160K. | **Update** |
| 4 | Backup steam avoided $27K/yr | **$52K/yr** | Steam with no storage 393 MWh/yr minus steam with storage 10 MWh/yr = 382 MWh × 3.41214 MMBtu/MWh × $40. The model simulates every hour, so storage also shaves demand peaks, not only the 200 outage hours. The old figure counted outage hours only. | **Update** |
| 5a | Storage payback ~6.7 yr | **6.9 yr** (floor credit on, condenser side) / **14.9 yr** (default, floor credit off) | `finance.storage_value`: (net cost $1.26M - avoided capture capex $0.48M) ÷ annual savings. Floor on: $52K steam + $60K floor = $112K/yr. Floor off: $52K/yr. | **Update** (6.9 yr with the floor credit; quote 14.9 yr as the default case) |
| 5b | Payback range 4.4-8.3 yr at $80-150/kWh | **3.2-9.8 yr** (floor credit on) / **6.9-20.9 yr** (floor credit off) | Same formula at $80/kWh (net $0.84M) and $150/kWh (net $1.575M) | **Update** |
| 6 | Full build-out $15.2M | **$15.18M** (rounds to $15.2M) | `finance.network`: hard costs × 1.25 | Holds |
| 6a | Pipe $7.2M | **$7.20M** | 1,200 ft × $6,000/ft | Holds |
| 6b | Soft costs $3.0M | **$3.04M** (rounds to $3.0M) | 25% × $12.14M hard costs | Holds |
| 6c | Capture $2.5M | **$2.50M** | Brief's $2.5M per 1.5 MW, our own estimate for heat exchangers, pumps and controls (ASSUMPTION). Scaled with exponent 0.6 (ASSUMPTION), which has no effect at 1.5 MW. | Holds |
| 6d | Battery $1.44M | **$1.44M** | 12 MWh × $120/kWh, before soft costs | Holds |
| 6e | Connections $1.0M | **$1.00M** | Fixed input | Holds |
| 7 | Heat sales ~$450K/yr | **$448K/yr** | 8,750 MWh/yr served × 3.41214 = 29,855 MMBtu (source side) × $15 | Holds |
| 8a | Cost per annual MMBtu ~$360 | **$490** (code's `cost_per_annual_mmbtu`) | Net capex to owner $14.64M ÷ 29,855 MMBtu of **source** heat sold. The old $360 divides **gross** capex $15.18M by 42,295 MMBtu of **delivered** heat (source × COP/(COP-1)), which gives $359. Both inputs are model outputs, but $490 is the figure the code reports, on the same source-side basis as the rest of the model. | **Update** (or label $359 as "gross capex per delivered MMBtu") |
| 8b | Con Ed pilot ~$4,980 per annual MMBtu | **Not from model** | External figure from the Con Ed filing, as cited in `docs/team-brief.md`: $45.53M ÷ ~9,100 MMBtu/yr. That division gives about $5,000, not $4,980, so check the exact MMBtu figure in the filing. The brief does not say whether the pilot's MMBtu is source or delivered heat. | Check against the filing |
| 8c | 10x+ better than the pilot | **~10x** ($4,980 ÷ $490 = 10.2x); 13.9x on the old $359 basis | Ratio of 8b to 8a | Holds, barely, on the $490 basis. Say "about 10x", not "10x+". |
| 9 | Total with rebuild trenching $9.2M | **$9.18M** (rounds to $9.2M) | Same as row 6 with pipe at $2,000/ft (one-third of $6,000, from the brief's "pipe laid during rebuild site work" scenario). Pipe falls to $2.4M. Cost of heat in that case: $27/MMBtu. | Holds |

## Other headline numbers

| Number | Current value | How it is computed |
|---|---|---|
| DC heat share | **99.9%** | Share of the synthetic hot water load served by data center heat, directly or through storage (`model.summarize`, "DC heat share" KPI) |
| Steam backup | **10 MWh/yr** (393 MWh/yr with no storage) | Hourly simulation: demand storage can't cover is met by Con Ed steam. 200 h/yr of data center outages is an input (ASSUMPTION). |
| CO2 avoided | **1,372 t/yr** | 42,295 MMBtu delivered × 0.04493 tCO2/MMBtu steam, minus 3.65 GWh heat pump electricity × 0.000145 tCO2/kWh (LL97 2030 coefficients) |
| Water saved | **3.6M gal/yr** | 29,855 MMBtu source heat ÷ 8,300 Btu per gallon evaporated. Only applies if the building uses cooling towers (ASSUMPTION). |
| Floor area, tank vs PCM, loop side | **7.8x** | PCM 50 kWh/m³ ÷ water at a 5.6 C swing (brief). Tank 6,572 sq ft vs PCM 847 sq ft at the same 3.05 m height. |
| Floor area, tank vs PCM, condenser side | **3.5x** | PCM 50 kWh/m³ ÷ water at a 12.2 C swing, 87 to 65 F (ASSUMPTION). Tank 2,987 sq ft vs PCM 847 sq ft. Use this figure for the revised design. |
| Network cost of heat | **$46/MMBtu** (vs $15 price) | `finance.network` levelized cost: 6% over 30 years, O&M 2% of gross capex per year |

## Related figure the deck should also update

- **Avoided capture equipment:** the brief says about $1.07M. The model gives **$0.48M**, because it sizes capture without storage to
  the 99th percentile of synthetic demand (1.91 MW, not 1.64 × 1.0 MW), scales cost with exponent 0.6 (ASSUMPTION) and adds 25% soft costs.
  So the storage "nearly pays for itself on day one" line no longer holds: $0.78M of net cost remains after avoided capture.

## Reproduce

Open the app (`python -m streamlit run app.py`) at defaults. The KPI row and the Storage comparison and Financial model tabs show rows 1, 2c, 5a,
6, 7 and the headline numbers. For rows 3 and 5 (floor credit), tick "Credit floor space saved vs a water tank" under Economics.
For row 9, set Pipe cost to $2,000/ft. Rows 5b and 8a come straight from `finance.storage_value` and `finance.network`
at the same inputs.
