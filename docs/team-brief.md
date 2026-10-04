# Team Brief: Phase Change Thermal Batteries for Data Center Heat Reuse

Text extracted from docs/team-brief.pdf (Ryan Mehta). Tables keep their original column
layout. The PDF is the source of truth if anything here looks garbled.

## Figures revised by our simulation model (see CLAUDE.md, Key findings)
- PCM placement: the brief places the 84 F PCM on the shared ambient loop. Our model shows it
  barely charges in winter there, so the design moves it to the condenser water (hot) side.
- Storage capacity is not counted twice: a forecast-based reserve covers outages while the rest
  shaves daily peaks, instead of the brief's combined 8 h ride-through plus peak shaving.
- Storage payback: the brief's 4 to 8 years assumes linear capture costs and a floor-space credit
  vs a water tank. With sublinear costs and no floor credit, our model gives about 16 years.
- The 7.8 h NYCHA outage average mostly reflects building-level failures, which a battery at
  the data center does not fix. It covers heat-source outages only.

---

```text
Phase Change Thermal Batteries for Data Center Heat Reuse




  Phase Change Thermal Batteries for Data
  Center Heat Reuse
  NYU Hackathon briefing · ​Oct 3, 2026 · ​@Jenna


  Bottom line
  Put a 12 MWh phase change battery inside 111 8th Avenue and connect it to Con Ed's
  Chelsea heat network, so data center heat reaches the rebuilt Fulton Houses on
  residents' schedule instead of the servers'.

       The battery costs about $1.8M installed and $1.26M after the federal tax credit. It pays
       back in 4 to 8 years by shrinking the heat capture equipment, cutting backup steam
       use, and taking about one-eighth the floor space of a water tank.
       The full network costs about $15M. Heat sales alone don't cover Manhattan trenching,
       so it needs utility cost recovery like Con Ed's pilot or pipe laid during the rebuild. It still
       delivers more than 10 times more heat per capital dollar than the pilot.
       NYCHA gets hot water about 20% cheaper than steam, plus an 8-hour buffer that
       covers its typical outage. The data center gets heat payments at almost no capital cost,
       and saves about 3.6 million gallons of water a year if its plant uses cooling towers.
       The biggest risk is the timing of the contested Fulton rebuild. That is why the battery
       sits at the data center, where demolition can't strand it.


  Site choice: 111 8th Avenue
  Build at Site 1, 111 8th Avenue in Chelsea. It has a working template one avenue away,
  dense and growing heat demand, and the space shortage that makes phase change
  storage worth its price.

  A utility is already doing a version of this next door. Con Edison's Chelsea pilot is
  designed to capture heat from the data center at 85 10th Avenue and pipe it about 1,250
  feet along West 16th Street to three Fulton Houses buildings with 291 apartments (Con Ed
  Stage 2 filing). The same filing says a nearby Google-owned data center has expressed
  interest in joining the network. It doesn't name the building, but Google owns 111 8th
  Avenue and Chelsea Market across Ninth Avenue (Real Estate Business Online).




                                                                                                 Page 1 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  Our pitch is the second heat source for that network, with storage the pilot doesn't
  have. The Con Ed design buffers heat with ordinary hot water tanks and the pipe loop
  itself. Adding a phase change battery at 111 8th Avenue lets the network grow without new
  energy center buildings.

  The heat source is real but its exact size is not public. 111 8th Avenue hosts several
  colocation operators. Third-party listings put Digital Realty's JFK10 at about 18 MW (Data
  Center Map), DataBank LGA2 at 664 kW (Inflect), and Equinix NY9 at about 1 MW
  (Datacenters.com). JFK10 also now hosts New York's first quantum-AI data center with
  NVIDIA (Digital Realty). This briefing sizes the system on a conservative slice of that heat,
  not the full load.

  Demand next door is about to multiply. The Fulton and Elliott-Chelsea rebuild would
  replace all 2,056 public housing apartments and add up to 3,454 more, plus new
  healthcare facilities and community centers (New York YIMBY). New buildings can be
  designed for low-temperature heat from day one, which is far cheaper than retrofitting.

  Lansing is the weaker fit for this technology. TeraWulf's proposed Lake Hawkeye site is
  listed at 400 MW, a much bigger heat source (Data Center Tracker). But its heat users are
  spread out, land is cheap, and the facility isn't built yet, so the space-saving advantage of
  phase change storage matters much less there.

  The Lansing details widen the gap. TeraWulf says the campus will use a closed-loop
  system that runs mostly as dry air cooling (Ithaca Voice), so there are no cooling towers
  whose water a heat network could save. The nearest named institutional prospect,
  Lansing High School, sits about 6.5 miles from the plant in a straight line, based on our
  check of published coordinates. Community acceptance is shakier too, with a 17,000-
  signature petition against the project and two environmental groups suing to stop it
  (State of Politics).


  How it works
  A phase change battery stores heat by melting a salt and gives it back at a steady
  temperature when the salt refreezes. Here it sits between a data center that makes heat
  on its own schedule and neighbors who need heat on theirs.

  Think of ice in a cooler. It holds at 0°C the whole time it melts, soaking up a lot of heat
  without getting warmer. A phase change material (PCM) does the same thing at a warmer
  temperature. Calcium chloride hexahydrate, a common salt hydrate, melts at about 29°C




                                                                                           Page 2 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  (84°F) and absorbs about 190 kJ per kg doing it (How To Store Electricity, 2026 review).
  When the loop around it cools below 29°C, the salt recrystallizes and releases that heat at
  nearly the same temperature.

  This matters most on a low-temperature loop. Water stores heat only by changing
  temperature, about 1.16 kWh per cubic meter per °C (Thermal Energy HQ). The Con Ed
  design lets the loop swing at most 10°F (5.6°C) between supply and return, so a water
  tank on that loop holds only about 6.5 kWh per cubic meter. Salt hydrates hold 45 to 120
  kWh per cubic meter (ORNL). After leaving room for heat exchanger tubes, that is still
  roughly 7 to 10 times more heat per cubic meter than water, which is the whole case for
  using PCM in a Manhattan basement.

  The same narrow band is the hardest part of the engineering. The PCM's melting point
  has to sit between the loop's supply and return temperatures, which are at most 10°F
  apart, so there are only a few degrees of driving force on each side. Salt hydrates also
  conduct heat poorly, so moving enough heat in and out takes a lot of heat exchanger
  surface (DOE). DOE-funded work is blending salt hydrates with compressed expanded
  graphite to fix that conductivity problem. Before ordering, the vendor should guarantee
  usable kWh and discharge kW at the loop's actual supply and return temperatures, not
  just the nameplate rating. A well-insulated PCM battery returns about 80 to 92% of the
  heat it stores on daily cycles (How To Store Electricity).

  Servers heat the data center's chilled water loop. Its chillers move that heat into
  condenser water, which normally goes to rooftop cooling towers. A side-stream heat
  exchanger sends some of it into a shared ambient loop that runs about 54 to 97°F in
  heating season (Con Ed filing). The PCM battery charges when the loop runs warm and
  discharges when it runs cool. Water-source heat pumps in each building then lift that heat
  to 140 to 170°F for hot water and space heat, at a COP around 3.4, meaning about 3.4 units
  of heat per unit of electricity (Trane via NEEA).




                                                                                        Page 3 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  heat chain from data halls to homes, with the battery on the shared loop

  Heat flows top to bottom. The battery hangs off the shared loop, while the cooling towers
  and Con Ed steam stay in place as backstops on either side.

  Salt hydrates have three known failure modes, and each has a standard fix (How To Store
  Electricity):

       Supercooling, where the liquid refuses to freeze at its melting point, is fixed with
       nucleating agents that seed crystals.
       Phase separation, where the salt and water drift apart over many cycles, is fixed with
       thickeners or crystal modifiers.
       Corrosion of metal containers is avoided with polypropylene or HDPE containment,
       which works below 100°C.

  Paraffin waxes avoid those problems but are flammable, which is a hard sell for NYC fire
  code in a residential basement. That is why this design uses a salt hydrate.




                                                                                              Page 4 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  The proven fallback is ice. Ice is the oldest commercial PCM, and Rockefeller Center
  already runs a 41-tank ice system with 8,600 ton-hours of storage (Reuters Events). Ice
  stores at 0°C, though, so heat pumps would work harder to lift it, and efficiency drops to a
  COP near 3.2.


  Customers and whether they actually need it
  The anchor customer is the rebuilt Fulton Houses next door, because hot water demand
  runs all year and matches a data center's flat output. Commercial buildings facing carbon
  fines come second and can pay a higher rate.


     Rank         Customer                                  What they need              Why they would buy

     1            New NYCHA replacement                     Hot water all year, plus    The PACT partners have
                  buildings on the Fulton                   space heat. The first new   told Con Ed they are
                  campus                                    building, at West 17th      interested in connecting
                                                            Street and Ninth Avenue,    this building for hot water.
                                                            is planned at about 391     Joining the network cuts
                                                            apartments and would        its electric peak by 137 to
                                                            need about 2,610 MMBtu      205 kW compared with
                                                            of hot water a year (Con    air-source heat pumps.
                                                            Ed filing)

     2            Existing Fulton pilot                     Hot water now, until        A second heat source
                  buildings (291                            demolition around 2032      plus storage gives the
                  apartments)                                                           pilot backup it currently
                                                                                        gets only from Con Ed
                                                                                        steam.

     3            Mixed-income rebuild                      Up to 3,454 new             New buildings can be
                  buildings, new healthcare                 apartments plus             designed for low-
                  facilities and community                  community space (New        temperature heat from
                  centers                                   York YIMBY)                 day one instead of buying
                                                                                        rooftop heat pumps.




                                                                                                                Page 5 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Rank         Customer                                  What they need              Why they would buy

     4            Chelsea Market (Google-                   Hot water for a food hall   It sits across Ninth
                  owned, 1.2 million sq ft)                 with more than 500,000      Avenue from the heat
                                                            visitors a month (CRE       source, and buildings over
                                                            Tech)                       25,000 sq ft pay $268 per
                                                                                        ton of carbon over their
                                                                                        Local Law 97 limit
                                                                                        (Facilities Dive).

     5            Google's own offices                      Winter space heat           Self-supply with no street
                  inside 111 8th Avenue                                                 pipe at all, but it is winter-
                                                                                        only and does nothing for
                                                                                        the community.


  The need is real and measurable. NYCHA logged 2,240 heat or hot water outages across
  its portfolio in the 2025-26 season, with a 7.8-hour average restoration time (NYCHA).
  City rules require hot water at 120°F at the source all year (NYCHA Journal). The Fulton
  census tract ranks in the 91st percentile for environmental burden, and 80% of Fulton
  residents are low to moderate income (Con Ed filing).

  Steam, the current heat source, keeps getting more expensive. Con Ed's example bill for
  an apartment building using 900 Mlb of steam a month rose from $28,659 in 2023-24 to
  $35,840 in 2025-26, about 25% in two years (Con Edison).

  Customer timing is the biggest uncertainty in this plan. The redevelopment was paused
  by an appeals court in March 2026 and cleared to proceed in July (City Limits), and some
  residents still oppose it (The City).


  How supply matches demand
  The brief asks teams to match supply and demand on five dimensions. The battery is what
  closes the gap on three of them.




                                                                                                                 Page 6 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Dimension                 Data center supply           Customer demand          How the design closes
                                                                                     the gap

     Temperature               Shared loop runs about       Hot water is made at     Building heat pumps
                               54 to 97°F                   about 170°F and          lift the heat. The PCM
                                                            mixed down to 120°F      melts at 84°F, in the
                                                                                     middle of the loop's
                                                                                     range.

     Capacity                  About 1.5 MW captured        Peaks run about 1.64     The battery covers the
                               from one tenant's            times the daily          peaks, so capture is
                               cooling plant (our           average, based on        sized to the average
                               assumption)                  Fulton's measured hot    instead of the peak.
                                                            water data

     Timing                    Data halls run around        Hot water peaks in the   The battery charges
                               the clock                    morning and evening      overnight and midday,
                                                                                     then discharges at the
                                                                                     peaks.

     Seasonality               Flat all year                Space heat is winter-    Hot water is the
                                                            only, but hot water is   anchor load. Summer
                                                            year-round               surplus simply stays in
                                                                                     the cooling towers.

     Continuity                Maintenance windows,         Hot water is legally     Eight hours of storage
                               economizer hours and         required all year        covers NYCHA's 7.8-
                               tenant changes                                        hour average outage.
                               interrupt supply                                      Con Ed steam stays
                                                                                     connected as the last
                                                                                     resort.




  Implementation at 111 8th Avenue
  Put the heat capture and the battery inside 111 8th Avenue, then run a short pipe west to
  the Con Ed network on the Fulton campus. Keeping the battery at the source means it
  survives the Fulton demolition, which is the main thing the Con Ed pilot could not protect
  against.




                                                                                                        Page 7 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  Putting the battery at the source has one trade-off. A battery at each customer building
  would also shave peaks off the pipe, but the Con Ed pipe is already oversized, 10-inch
  instead of the 6-inch the pilot needs (Con Ed filing), so that benefit is small here.


  System at a glance

     Component                     Size (our estimate)        Location              Owner

     Heat capture                  Side-stream plate heat     111 8th Ave cellar    Network owner, with
                                   exchanger on one                                 the data center
                                   tenant's condenser                               owning everything on
                                   water loop, about 1.5                            its side of an isolation
                                   MW (5,100 MBH)                                   valve

     Phase change                  12 MWh of salt hydrate     111 8th Ave cellar,   Network owner or a
     battery                       melting at 84°F, which     about 240 m³ or 860   storage-as-a-service
                                   is 8 hours at full         sq ft at 10 ft tall   partner
                                   capture

     Pumps and                     Redundant (N+1)            111 8th Ave cellar    Network owner
     controls                      pumps, metering, and
                                   controls tied into Con
                                   Ed's monitoring
                                   system

     Distribution                  About 600 ft of trench     Street and Fulton     Network owner
                                   carrying 1,200 ft of       campus
                                   pre-insulated supply
                                   and return pipe,
                                   crossing Ninth Avenue
                                   to the pilot's isolation
                                   valves in the Fulton
                                   parking lot

     Customer                      Energy transfer            Each customer         Building owner
     connections                   stations and water-        building
                                   source heat pumps




                                                                                                         Page 8 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Component                     Size (our estimate)        Location        Owner

     Backup heat                   Con Ed steam heat          Fulton campus   Con Ed and building
                                   exchanger already                          owners
                                   designed into the pilot,
                                   plus steam or electric
                                   backup in new
                                   buildings


  The pipe length is a planning estimate. Check it against the GIS data in the hackathon
  resource list before presenting.

  The space comparison is the reason to use PCM. A water tank doing the same job on this
  narrow-temperature loop would need about 1,850 m³ and roughly 6,600 sq ft of floor,
  nearly 8 times the battery's footprint.


  Operating modes
   1. Overnight, hot water demand is low, so capture runs at full output and the surplus
      melts the PCM.
   2. During the morning and evening peaks, demand rises above what capture can supply,
       so the PCM refreezes and covers the difference.
   3. During data center maintenance or an outage, isolation valves close on the data center
      side and the battery carries the loop for up to about 8 hours at design load. Con Ed
       steam takes over only after that.
   4. In winter, the battery lets the data center keep its free cooling. At 85 10th Avenue,
      providing heat forced the building to run chillers instead of free cooling, which raised
      its electric bill (Con Ed filing). With storage, the data center can free-cool most hours
       and run chillers only in cheap overnight hours to charge the battery.


  Protecting data center cooling
  The network never becomes part of the data center's cooling path. Its cooling towers stay
  sized for 100% of heat rejection, and the network only takes heat the data center offers
  through a side-stream heat exchanger, so the two water loops never mix. On any fault,
  control valves fail toward the towers and condenser water goes back to its normal route.
  The data center operator keeps an override at the demarcation valve. The Con Ed pilot
  uses the same arrangement and expects the network to send heat back to the towers
  only about 10 hours a year.




                                                                                                Page 9 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  Phasing

     When                      Step

     2027                      Meter one tenant's condenser loop for two weeks,
                               as Con Ed did at 85 10th Avenue, and confirm
                               whether it uses cooling towers or liquid cooling,
                               since warmer liquid-cooling return water would
                               raise heat pump efficiency. Sign a heat exchange
                               agreement and petition the Public Service
                               Commission to add a second heat source to the
                               Chelsea network.

     2028                      Install capture and the battery inside 111 8th
                               Avenue. This needs no street work.

     2029 to 2031              Lay the pipe while the rebuild's site work is already
                               open, then connect the first new NYCHA building.

     2032 to 2034              Connect the remaining rebuild buildings and
                               Chelsea Market. Build the storage before the end
                               of 2032 to stay inside the full tax credit window,
                               and confirm the exact timing rule with a tax
                               advisor.




  Where the materials come from
  The storage material itself is a cheap, US-made commodity salt. The supply risk sits in the
  engineered product around it: the containers, heat exchangers and controls, which come
  from a small number of specialist vendors.


     Part                                What it is                         Where it comes from

     Base salt                           Calcium chloride hexahydrate,      Made in the US from natural
                                         the same calcium chloride used     underground brines, with
                                         on icy roads, melting near 84°F    Michigan the leading region, and
                                                                            as a byproduct of soda ash
                                                                            production (IMARC)




                                                                                                        Page 10 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Part                                What it is                           Where it comes from

     Additives                           A few percent of a nucleating salt   Specialty chemical suppliers,
                                         to prevent supercooling, plus a      usually blended by the PCM
                                         thickener to stop the salt and       vendor
                                         water separating

     Containment                         Sealed HDPE or polypropylene         Plastics molders, usually through
                                         panels or capsules, which resist     the PCM vendor
                                         salt corrosion below 100°C

     Tank and heat                       An insulated tank where loop         Mechanical contractors and
     exchanger                           water flows around the sealed        HVAC suppliers
                                         PCM


  Several vendors already sell salt hydrate PCMs in this temperature range. Climator
  (Sweden) sells the ClimSel salt hydrate line, PLUSS (India) sells savE salt hydrates, and
  Croda (UK) sells plant-based CrodaTherm grades (How To Store Electricity). In the US,
  Insolcorp is a partner on a Department of Energy project building salt hydrate thermal
  batteries for commercial heat pumps (DOE).

  Buying domestic pays twice. A US-made product raises the federal tax credit from 30%
  to as much as 40% through the domestic content bonus (Trane via NEEA). It also avoids
  tariff and sourcing risk on imported equipment.

  Specify certified material. The German RAL quality mark (RAL-GZ 896) independently
  tests latent heat, melting point and cycle stability across at least 10,000 cycles (How To
  Store Electricity). Require it, or equivalent test data, in the procurement spec along with a
  cycle-life warranty.

  End of life is easy. Calcium chloride is non-toxic and is sold in bulk as road de-icer and
  dust control, so spent material can be reused instead of landfilled. That is a good line for
  the brief's resource optimization criterion.


  Financial ROI
  The battery itself pays back in roughly 4 to 8 years. The full heat network does not pay
  back on heat sales alone at Manhattan trenching costs, so it needs the same utility cost
  recovery Con Ed's pilot uses, or pipe laid during the rebuild's site work. All figures below
  are planning estimates built from the cited benchmarks, not quotes.




                                                                                                           Page 11 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  The battery on its own

     Item                                                   Value                           Basis

     Installed cost                                         $1.8M                           12 MWh at $120/kWh plus 25%
                                                                                            soft costs. Installed commercial
                                                                                            PCM runs about $80 to
                                                                                            $150/kWh (How To Store
                                                                                            Electricity).

     Federal tax credit                                     minus $0.54M                    30% base investment tax credit
                                                                                            for thermal storage with
                                                                                            prevailing wages, available
                                                                                            through 2032 (Trane via NEEA)

     Net cost                                               $1.26M

     Avoided capture equipment                              about $1.07M, one time          Without storage, capture must
                                                                                            be sized to the 1.64x peak. That
                                                                                            is 0.64 MW more equipment at
                                                                                            our assumed $1,667/kW.

     Avoided backup steam                                   about $27K a year               Assumes 200 hours a year of
                                                                                            data center downtime at 1 MW,
                                                                                            with steam at $40/MMBtu

     Floor space saved compared                             about 5,800 sq ft, worth        Valued at $28/sq ft, one-third of
     with a water tank                                      about $160K a year              Midtown South's $84.77 office
                                                                                            asking rent (Metro Manhattan
                                                                                            citing CBRE)


  Compared with having no storage, the battery nearly pays for itself on day one. The
  avoided capture equipment covers all but about $0.19M of its net cost, and avoided steam
  covers the rest in about 7 years. The 8 hours of ride-through for residents comes on top of
  that.

  Compared with a water tank, the space savings and avoided steam add up to about $189K
  a year, which pays back the full net cost in about 6.7 years. That figure is conservative
  because it ignores what the water tank itself would cost.


     Installed PCM cost                  Net cost after 30% credit              Payback against a water tank

     $80/kWh                             $0.84M                                 4.4 years



                                                                                                                        Page 12 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Installed PCM cost                  Net cost after 30% credit        Payback against a water tank

     $120/kWh (base)                     $1.26M                           6.7 years

     $150/kWh                            $1.57M                           8.3 years



  The full network

     Capital item                                     Cost     Basis

     Heat capture at 111 8th Ave                      $2.5M    Our assumption for heat exchangers, pumps and
                                                               controls

     Phase change battery                             $1.44M   12 MWh at $120/kWh

     Distribution pipe                                $7.2M    1,200 ft at $6,000/ft. Con Ed's pilot budgets about
                                                               $19M, including pumps and contingency, for its
                                                               2,500 ft of pipe (Con Ed filing).

     Customer connections                             $1.0M    Energy transfer stations only. New buildings buy
                                                               their own heat pumps either way.

     Soft costs and contingency                       $3.0M    25%

     Total                                            $15.2M


  At full build-out the network sells an average of 1.0 MW of source heat, about 29,900
  MMBtu a year. The price NYCHA can pay and still save money against steam is about
  $15/MMBtu, which brings in about $450K a year. The cost of producing that heat depends
  almost entirely on the pipe and on how much heat is sold.


     Scenario                                                   Total         Average heat      Cost of heat
                                                                capital       sold              ($/MMBtu)

     Street trench, base load                                   $15.2M        1.0 MW            $46

     Street trench, more customers                              $15.2M        1.4 MW            $33

     Pipe laid during rebuild site work at                      $9.2M         1.0 MW            $27
     one-third the cost

     Rebuild site work and more customers                       $9.2M         1.4 MW            $19




                                                                                                                Page 13 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  The cost of heat assumes a 6% cost of capital over 30 years, operations and maintenance
  at 2% of capital a year, and the tax credit on the storage. Even the best case sits above
  the $15 affordable price, so three levers close the gap:

       Utility cost recovery is the first lever. Con Ed is recovering its pilot's cost from electric
       ratepayers, arguing that heat networks reduce the grid's peak demand (Con Ed filing).
       The pilot costs $45.53M to serve about 9,100 MMBtu of heat a year, roughly $4,980 of
       capital per annual MMBtu. This design costs about $360 per annual MMBtu, more than
       10 times better, because it reuses the pilot's pipe and serves new buildings instead of
       retrofitting old ones.
       Two-tier pricing is the second lever. NYCHA pays the affordable $15 rate, while
       commercial customers facing Local Law 97 fines, like Chelsea Market, pay closer to the
       full cost of heat.
       Digging once is the third. Coordinating the trench with the rebuild's own excavation
       cuts the biggest cost line.


  Value for each stakeholder
  NYCHA saves about 20% on hot water compared with steam. Each MMBtu of hot water
  from the network costs about $21.50 in heat pump electricity at $0.25/kWh, plus about
  $10.60 in network charges, for about $32 in total. Steam costs about $40, using Con Ed's
  apartment-house example and treating 1 Mlb of steam as roughly 1 MMBtu of usable heat.
  New all-electric buildings would pay about the same as with air-source heat pumps, about
  $33, but with a lower electric peak and no rooftop equipment. New York commercial
  electricity averaged 22 to 24 cents per kWh statewide in early 2026 (NYSERDA), and
  Manhattan runs higher, so $0.25 is a working assumption.

  The data center gets paid and saves water at almost no capital cost. In the Con Ed
  model, the utility pays the building owner for heat to cover any added electricity plus a
  modest return. If the tenant's plant uses cooling towers like 85 10th Avenue does,
  diverting an average of 1 MW from them also avoids roughly 3.6 million gallons of
  evaporation a year, our estimate at about 8,300 Btu per gallon evaporated. Confirm the
  cooling type during metering, because an air-cooled plant saves no water this way.

  The community gets lower carbon and fewer cold showers. Using Local Law 97's 2030
  emission factors (Legal Clarity), each MMBtu of hot water shifted off steam saves about
  0.032 tons of CO2. At full build-out that is up to about 1,370 tons a year if all the heat
  displaces steam, or about 290 tons if it all displaces air-source heat pumps. The real
  number lands in between, and the 8-hour buffer protects residents from the typical
  outage.


                                                                                              Page 14 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




  Risks, ownership and who carries what
  The network owner carries the construction and performance risk, and gets a regulated
  return for it. Everyone else carries a small, specific risk tied to what they control.


     Stakeholder                      Pays for                     Gets                     Risk they carry

     Google, owner of                 Cellar space leased to       Lease income, water      Minimal, because the
     111 8th Ave                      the network owner            savings and a visible    network is a side-
                                                                   community project        stream and the towers
                                                                                            stay in place

     Colocation                       Pipe taps on its own         Heat payments            Coordinating
     tenant supplying                 side of the                  covering added           maintenance windows
     heat                             demarcation valve            electricity plus a
                                                                   modest return

     Con Ed or                        Capture, battery,            Regulated return on      Construction cost and
     another network                  pipe, pumps and              the asset, plus heat     system performance
     owner                            controls                     sales

     NYCHA and its                    Water-source heat            About 20% cheaper        Rebuild timing
     PACT partners                    pumps in new                 hot water than
                                      buildings, which they        steam and an 8-hour
                                      need anyway                  buffer

     Chelsea Market                   Its own connection           A path to Local Law      Paying the higher
                                                                   97 compliance            commercial rate

     PCM vendor                       Cycle-life and               The equipment sale       Material degradation
                                      capacity warranty



     Risk                                        What could happen                 Mitigation

     Rebuild delay                               Court challenges or relocation    Install capture and storage
                                                 fights push customer              inside 111 8th Ave first, and
                                                 connections back years            serve the existing pilot
                                                                                   buildings in the meantime




                                                                                                                Page 15 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




     Risk                                        What could happen                  Mitigation

     Data center changes                         At 85 10th Ave, a switch to        Storage allows off-peak
     how it runs                                 winter free cooling cut            charging, the contract sets a
                                                 available heat and raised costs    minimum heat offer, and other
                                                                                    tenants in the building are
                                                                                    alternate sources

     PCM wears out                               Supercooling or salt separation    Require RAL-certified material,
                                                 cuts capacity over time            a capacity warranty and an
                                                                                    annual capacity test

     Pipe cost overruns                          Unknown utilities under Ninth      Test pits before design, as Con
                                                 Avenue                             Ed did on West 16th Street, and
                                                                                    lay pipe during rebuild
                                                                                    excavation

     Regulatory delay                            The Chelsea pilot was still in     Frame the project as an
                                                 design, stage two of five, as of   expansion of an already-
                                                 July 2026 (Ecosystem)              designed network

     Tax credit phases down                      The storage loses part of its      Start construction on the
     after 2032                                  30% credit                         storage before the end of 2032

     Cybersecurity                               A utility control link becomes a   Keep only metering between
                                                 path into the data center          the two, with local control
                                                                                    panels, which is the approach
                                                                                    Con Ed chose for the pilot

     Resident trust                              Residents see the project as       NYCHA stays the customer of
                                                 tied to a contested rebuild        record so tenants are never
                                                                                    billed, as in the pilot, and
                                                                                    residents get in-unit
                                                                                    temperature control




  Sources
  Site and network

       Con Edison, Chelsea UTEN Stage 2 Filing, July 2025
       Con Edison, Chelsea Thermal Energy Network
       Ecosystem, Con Edison UTEN pilots



                                                                                                               Page 16 of 17
Phase Change Thermal Batteries for Data Center Heat Reuse




       Digital Realty, JFK10 at 111 8th Avenue
       Data Center Tracker, 111 8th Avenue listing
       Inflect, DataBank LGA2
       Datacenters.com, Equinix NY9
       Real Estate Business Online, Google buys Chelsea Market
       CRE Tech, Google closes Chelsea Market purchase

  Customers and community

       New York YIMBY, HUD approves Fulton and Elliott-Chelsea redevelopment
       City Limits, court lifts pause on redevelopment
       The City, NYCHA holdouts at Fulton
       NYCHA, 2025-26 heat season results
       NYCHA Journal, heat season requirements
       Facilities Dive, Local Law 97 compliance period
       Legal Clarity, Local Law 97 emission coefficients

  Technology, materials and costs

       ORNL, salt hydrate PCM review
       How To Store Electricity, PCM storage deep dive 2026
       Thermal Energy HQ, thermal storage guide
       Trane via NEEA, HVAC thermal storage and the 48E tax credit, July 2026
       DOE, dual-purpose thermal battery project with Insolcorp
       Reuters Events, ice storage at Rockefeller Center
       IMARC, US calcium chloride market
       DOE, low-cost composite salt hydrate PCM

  Prices

       Con Edison, steam bill impacts
       NYSERDA, commercial electricity prices
       Metro Manhattan, Chelsea office rents citing CBRE

  Lansing comparison

       Ithaca Voice, Lansing planning board review of the data center plan
       State of Politics, proposed data centers dividing New Yorkers




                                                                                Page 17 of 17
```
