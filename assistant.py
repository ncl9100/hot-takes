"""'Ask the model' assistant: Claude answers judges' questions by calling read-only tools
that run the same heatsim pipeline as the dashboard. heatsim/ is not modified."""
import json
import re
from pathlib import Path

import numpy as np
from heatsim.model import Storage, simulate, summarize
from heatsim.forecast import reserve_policies, POLICY_NAMES
from heatsim import finance as fin

MODEL = "claude-sonnet-5-5"
MAX_TOKENS = 1000
MAX_TOOL_CALLS = 5
MAX_QUESTIONS = 15
MAX_INPUT_CHARS = 500
DOCS_DIR = Path(__file__).parent / "docs"

# Shown on the Assumptions tab and returned by get_assumptions().
ASSUMPTIONS_MD = """
- **Heat source:** 1.5 MW captured from one tenant's condenser loop at 111 8th Ave. ASSUMPTION; the building's cooling plant data is not public. Must be metered.
- **Demand:** synthetic hourly hot water profile with the brief's 1.64 peak-to-average ratio, seasonal inlet temperature effect and random variation. Not metered data.
- **Loop temperatures:** 54 to 97 F seasonal range and 10 F supply/return swing from the Con Ed Stage 2 filing; seasonal shape is our assumption. Condenser water at 90 F is our assumption.
- **Storage:** salt hydrate (CaCl2.6H2O, ~84 F melt, ~50 kWh/m3 system density), 86% round trip, 1%/day standby loss. Charge/discharge power 2.5 MW by default, sized to peak demand (ASSUMPTION). Water tank comparison: 5.6 C swing on the loop side (brief), 87 to 65 F swing on the condenser side (ASSUMPTION).
- **Costs:** capture $2.5M per 1.5 MW scaled with exponent 0.6; storage $120/kWh; pipe $6,000/ft x 1,200 ft; 25% soft costs; 30% ITC on storage; 6% over 30 years; O&M 2%/yr.
- **Carbon:** NYC Local Law 97 2030 coefficients. **Water:** ~8,300 Btu per gallon evaporated, only if the plant uses cooling towers.
"""

PROVENANCE = ("Hourly demand and weather are SYNTHETIC profiles calibrated to the team brief (docs/team-brief.md), "
              "not metered data. Forecast errors mostly reflect injected noise. Costs, prices and coefficients come "
              "from the brief and organizer materials (docs/) unless marked ASSUMPTION. All power values are "
              "source-side heat in MW thermal; delivered heat = source x COP/(COP-1), COP 3.4.")

# Default values and where each comes from (returned by get_assumptions). "docs/..." = team research files.
SOURCES = [
    ("Heat capture capacity", "1.5 MW", "Team brief estimate for one tenant's condenser loop; not public, must be metered (ASSUMPTION)"),
    ("Capture cost", "$2.5M per 1.5 MW, scaled with exponent 0.6", "Team brief estimate for heat exchangers, pumps and controls (ASSUMPTION); exponent is ASSUMPTION"),
    ("Storage capacity", "12 MWh (8 h at full capture)", "Team brief design basis"),
    ("PCM energy density", "50 kWh/m3 system", "Team brief: 12 MWh in about 240 m3"),
    ("PCM melt point", "84 F (CaCl2.6H2O salt hydrate)", "Team brief"),
    ("Round trip efficiency", "86%", "Midpoint of the brief's 80-92% for daily cycles (How To Store Electricity, cited in team brief)"),
    ("Standby loss", "1%/day", "ASSUMPTION"),
    ("Storage charge/discharge power", "2.5 MW", "Sized to peak demand (ASSUMPTION)"),
    ("Installed storage cost", "$120/kWh", "Team brief range $80-150/kWh installed PCM"),
    ("Shared loop temperature", "54-97 F seasonal, 10 F supply/return swing", "Con Ed Stage 2 filing (cited in team brief); seasonal shape is ASSUMPTION"),
    ("Condenser water temperature", "90 F", "ASSUMPTION; verify by metering"),
    ("Water tank swing, condenser side", "87 to 65 F", "ASSUMPTION"),
    ("Water tank swing, loop side", "5.6 C (10 F)", "Team brief, from the loop's supply/return swing"),
    ("Peak-to-average demand", "1.64", "Team brief, from Fulton data"),
    ("Hourly demand and weather", "synthetic profiles", "SYNTHETIC, calibrated to the team brief; not metered"),
    ("Data center heat outages", "200 h/yr", "Team brief assumption (ASSUMPTION input)"),
    ("Heat pump COP", "3.4", "Trane via NEEA (cited in team brief)"),
    ("NYCHA heat price", "$15/MMBtu source heat", "Team brief: price NYCHA can pay and still save against steam"),
    ("Commercial heat price", "$35/MMBtu", "ASSUMPTION"),
    ("Con Ed steam price", "$40/MMBtu", "Con Ed bill example in the team brief, treating 1 Mlb as about 1 MMBtu (ASSUMPTION)"),
    ("Electricity price", "$0.25/kWh", "Working assumption (ASSUMPTION)"),
    ("Distribution pipe", "1,200 ft at $6,000/ft", "Team brief (context: Con Ed pilot budgets about $19M for 2,500 ft, Con Ed filing)"),
    ("Pipe laid during rebuild", "about $2,000/ft", "One-third of $6,000, from the brief's rebuild site-work scenario (docs/slide-numbers.md)"),
    ("Customer connections", "$1.0M", "Team brief: energy transfer stations only; buildings buy their own heat pumps"),
    ("Soft costs and contingency", "25%", "Team brief"),
    ("Investment tax credit on storage", "30%", "48E base ITC (team brief)"),
    ("Cost of capital and life", "6% over 30 years", "Team brief"),
    ("O&M", "2% of gross capex per year", "Team model (docs/slide-numbers.md)"),
    ("Carbon coefficients", "steam 0.04493 tCO2/MMBtu, electricity 0.000145 tCO2/kWh", "NYC Local Law 97, 2030 coefficients"),
    ("Water saved", "8,300 Btu per gallon evaporated", "Team estimate; only if the plant uses cooling towers"),
    ("Floor space value", "$28/sq ft per year", "One-third of Midtown South asking rent (ASSUMPTION); credit off by default"),
]

# name: (type, min or choices, max, description). Same names and ranges as the sidebar.
PARAMS = {
    "capture_mw": ("number", 0.5, 3.0, "Heat capture capacity, MW"),
    "avg_demand_mw": ("number", 0.3, 2.0, "Average heat demand, source side, MW"),
    "space_heat_share": ("number", 0.0, 0.6, "Space heating share of load (0 = hot water only)"),
    "storage_kind": ("string", ["pcm", "water", "none"], None, "Storage technology"),
    "storage_mwh": ("number", 0.0, 24.0, "Storage capacity, MWh"),
    "storage_power_mw": ("number", 0.5, 4.0, "Storage charge/discharge power, MW (ASSUMPTION default 2.5)"),
    "placement": ("string", ["condenser", "loop"], None,
                  "Storage placement: condenser water (revised design) or shared ambient loop (original brief)"),
    "melt_f": ("number", 70, 95, "PCM melt point, F"),
    "outage_hours": ("number", 0, 600, "Data center heat outages, h/yr"),
    "reserve_policy": ("string", POLICY_NAMES, None, "Outage reserve policy"),
    "ride_through_h": ("number", 2, 12, "Ride-through target, h"),
    "heat_price": ("number", 5.0, 50.0, "NYCHA heat price, $/MMBtu source heat"),
    "commercial_share": ("number", 0.0, 0.6, "Share of heat sold to commercial (LL97) buyers"),
    "commercial_price": ("number", 15.0, 60.0, "Commercial heat price, $/MMBtu"),
    "storage_cost_per_kwh": ("number", 40, 200, "Installed storage cost, $/kWh (team brief: $80-150/kWh installed PCM)"),
    "pipe_cost_per_ft": ("number", 1000, 10000, "Pipe cost, $/ft (~$2,000 if laid during the rebuild site work)"),
    "ratepayer_share": ("number", 0.0, 1.0, "Share of capex recovered via utility rates"),
    "elec_price": ("number", 0.10, 0.40, "Electricity price, $/kWh"),
    "steam_price": ("number", 20.0, 60.0, "Con Ed steam price, $/MMBtu"),
    "credit_floor_space": ("boolean", None, None, "Credit floor space saved vs a water tank"),
}


def _param_schema():
    props = {}
    for name, (typ, lo, hi, desc) in PARAMS.items():
        p = {"type": typ, "description": desc}
        if isinstance(lo, list):
            p["enum"] = lo
        elif typ == "number":
            p["minimum"], p["maximum"] = lo, hi
        props[name] = p
    return {"type": "object", "properties": props, "additionalProperties": False}


TOOLS = [
    {"name": "run_scenario",
     "description": "Run the 8,760-hour simulation plus finance model and return KPIs. Any parameter you omit keeps "
                    "the judge's current dashboard setting, so call with {} to get the current dashboard numbers. "
                    "Returns settings_used, DC heat share, steam backup MWh/yr, NYCHA cost, CO2 avoided, cost of heat, "
                    "NPV, network payback, storage payback and floor areas.",
     "input_schema": {"type": "object", "properties": {"params": _param_schema()}, "required": ["params"],
                      "additionalProperties": False}},
    {"name": "compare_scenarios",
     "description": "Run 2 to 6 scenarios side by side (each a set of parameter overrides on top of the current "
                    "dashboard settings) and return one row of KPIs per scenario. Include a baseline ({} params) "
                    "when the question is 'what if'.",
     "input_schema": {"type": "object", "properties": {"scenarios": {
         "type": "array", "minItems": 2, "maxItems": 6,
         "items": {"type": "object", "properties": {"label": {"type": "string"}, "params": _param_schema()},
                   "required": ["label", "params"], "additionalProperties": False}}},
         "required": ["scenarios"], "additionalProperties": False}},
    {"name": "get_assumptions",
     "description": "Return the model's assumption list, data provenance, every default value with its source, and "
                    "the parameter names, ranges and current dashboard values.",
     "input_schema": {"type": "object", "properties": {}, "additionalProperties": False}},
    {"name": "search_docs",
     "description": "Keyword search over the team's research documents (team brief, organizer materials review, "
                    "judging criteria, technical research, slide numbers). Returns matching passages with file "
                    "names. Use for site facts, costs, sources, and anything the simulation does not compute.",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string", "description": "Keywords"}},
                      "required": ["query"], "additionalProperties": False}},
]

SYSTEM = """You are the ChelseaHeat assistant in a hackathon demo app. Judges ask you questions about the design and its numbers.

How the system works (use this wording; do not add equipment that is not listed):
- Source: servers at the 111 8th Ave data center heat its chilled water; its chillers reject that heat into condenser water, which normally goes to rooftop cooling towers.
- Capture: a side-stream plate heat exchanger in the 111 8th Ave cellar takes heat from one tenant's condenser water loop. The two water loops never mix, the cooling towers stay sized for all of the heat, and valves fail back toward the towers. There is no heat pump at the data center.
- Storage: a phase change (salt hydrate) thermal battery on the condenser water side of the heat exchanger (our revised design; the original brief put it on the shared loop, where it barely charges in winter). It charges from surplus heat and discharges at demand peaks and during data center heat outages.
- Distribution: the heat goes into Con Ed's Chelsea shared ambient loop and through pipe to the rebuilt NYCHA Fulton Houses.
- Use: water-source heat pumps in each customer building lift the loop heat to hot water temperatures.
- Backup: Con Ed steam covers whatever the network cannot.

Rules:
- Greetings, thanks or small talk: reply in one or two sentences and suggest two or three things you can help with (for example what-if scenarios, storage choices, costs and bills). Do not call tools for these.
- Every number you state must come from a tool result in this conversation or from a passage returned by search_docs (name the file). Never estimate, recall or extrapolate a number yourself. If you need a number, run the model with run_scenario or compare_scenarios, or get its source with get_assumptions.
- "What if" questions: compare against the current dashboard settings (params {}) so the judge sees the change.
- Demand and weather data are synthetic, calibrated to the brief, not metered. Say so whenever an answer depends on demand, steam, forecasts or anything derived from them. Values marked ASSUMPTION are the team's own assumptions; say so when they drive the answer.
- If a question is outside what the model and docs cover, say that plainly instead of guessing. Do not invent sources.
- Power is source-side heat in MW thermal; energy is in MWh. Never mix them up.
- Answer only the newest message. Answers: short and plain, with numbers and units. Aim for under 120 words plus at most one small table. No preamble, no offers of follow-up runs."""


def current_settings(**kw):
    """Map the sidebar's variables to tool parameter names."""
    return {k: kw[k] for k in PARAMS}


def _validate(params, base):
    p = dict(base)
    for k, v in (params or {}).items():
        if k not in PARAMS:
            raise ValueError(f"Unknown parameter '{k}'. Valid: {', '.join(PARAMS)}")
        typ, lo, hi, _ = PARAMS[k]
        if typ == "number":
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise ValueError(f"{k} must be a number")
            if not lo <= v <= hi:
                raise ValueError(f"{k}={v} is outside the model's range [{lo}, {hi}]")
        elif typ == "boolean" and not isinstance(v, bool):
            raise ValueError(f"{k} must be true or false")
        elif isinstance(lo, list) and v not in lo:
            raise ValueError(f"{k} must be one of {lo}")
        p[k] = v
    return p


def compute(p, base_data):
    """Same pipeline as the dashboard (app.py) for one set of parameters."""
    w, d, o, pred, profile, metrics = base_data(p["avg_demand_mw"], p["space_heat_share"], int(p["outage_hours"]))
    kind, cap = p["storage_kind"], p["capture_mw"]
    store = Storage(kind=kind, capacity_mwh=p["storage_mwh"] if kind != "none" else 0.0,
                    power_mw=p["storage_power_mw"], melt_f=p["melt_f"], placement=p["placement"])
    policies = reserve_policies(d, pred.values, profile.values, ride_through_h=int(p["ride_through_h"]))
    s = summarize(simulate(d, o, cap, store, policies[p["reserve_policy"]]))
    s_none = summarize(simulate(d, o, cap, Storage(kind="none")))
    f = fin.FinanceInputs(storage_cost_per_kwh=p["storage_cost_per_kwh"], pipe_cost_per_ft=p["pipe_cost_per_ft"],
                          heat_price=p["heat_price"], commercial_share=p["commercial_share"],
                          commercial_price=p["commercial_price"], ratepayer_share=p["ratepayer_share"],
                          elec_price=p["elec_price"], steam_price=p["steam_price"],
                          count_floor_space=p["credit_floor_space"])
    net = fin.network(s, cap, store.capacity_mwh, f)
    cust = fin.customer(f)
    imp = fin.impact(s, f)
    tank = Storage(kind="water", capacity_mwh=p["storage_mwh"], power_mw=p["storage_power_mw"],
                   placement=p["placement"])
    sv = fin.storage_value(s, s_none, float(np.percentile(d, 99)), cap, store, tank, f)
    r = lambda x, n=1: None if x is None or not np.isfinite(x) else round(float(x), n)
    return {
        "dc_heat_share_pct": r(100 * s["network_share"], 1),
        "steam_backup_mwh_per_yr": r(s["steam_mwh"]),
        "steam_backup_no_storage_mwh_per_yr": r(s_none["steam_mwh"]),
        "steam_mwh_during_outages": r(s["steam_mwh_during_outages"]),
        "steam_hours_per_yr": s["steam_hours"],
        "nycha_cost_usd_per_mmbtu": r(cust["total"], 2),
        "con_ed_steam_usd_per_mmbtu": r(cust["steam"], 2),
        "nycha_savings_vs_steam_pct": r(100 * cust["savings_pct"]),
        "co2_avoided_t_per_yr": r(imp["tco2_avoided_vs_steam"], 0),
        "water_saved_million_gal_per_yr": r(imp["water_gal_saved"] / 1e6, 2),
        "cost_of_heat_usd_per_mmbtu": r(net["lcoh"]),
        "avg_heat_price_usd_per_mmbtu": r(net["avg_price"]),
        "capex_gross_musd": r(net["capex_gross"] / 1e6, 2),
        "capex_net_to_owner_musd": r(net["capex_net_to_owner"] / 1e6, 2),
        "npv_30yr_6pct_musd": r(net["npv"] / 1e6, 2),
        "network_payback_years": net["payback_years"] if net["payback_years"] is not None else "beyond 30 yr",
        "storage_net_capex_musd": r(sv["storage_capex_net"] / 1e6, 2),
        "storage_annual_savings_kusd": r((sv["annual_steam_savings"] + sv["annual_floor_value"]) / 1e3),
        "storage_payback_years": r(sv["payback_years"]) if np.isfinite(sv["payback_years"]) else "n/a (no savings)",
        "storage_floor_area_sqft": r(store.footprint_sqft(), 0),
        "water_tank_same_energy_floor_area_sqft": r(tank.footprint_sqft(), 0),
    }


def search_docs(query, k=5, max_chars=900):
    terms = [t for t in re.findall(r"[a-z0-9$.]+", query.lower()) if len(t) > 2 or t.isdigit()]
    hits = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        if path.name == "CLAUDE.md":  # agent instructions, not research
            continue
        heading = ""
        for para in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
            line = para.strip()
            if line.startswith("#"):
                heading = line.splitlines()[0].lstrip("# ").strip()
            low = para.lower()
            score = sum(low.count(t) for t in terms) + 2 * sum(t in low for t in terms)
            if score:
                hits.append((score, path.name, heading, line[:max_chars]))
    hits.sort(key=lambda h: -h[0])
    if not hits:
        return {"results": [], "note": "No matching passages in docs/."}
    return {"results": [{"file": f"docs/{n}", "section": h, "passage": t} for _, n, h, t in hits[:k]]}


def run_tool(name, args, base, base_data):
    if name == "run_scenario":
        p = _validate(args.get("params"), base)
        return {"settings_used": p, "kpis": compute(p, base_data), "data_note": "Demand and weather are synthetic."}
    if name == "compare_scenarios":
        rows = []
        for sc in args.get("scenarios", [])[:6]:
            p = _validate(sc.get("params"), base)
            rows.append({"label": sc.get("label", ""), "overrides": sc.get("params") or {}, **compute(p, base_data)})
        return {"rows": rows, "data_note": "Demand and weather are synthetic."}
    if name == "get_assumptions":
        return {"assumptions": ASSUMPTIONS_MD.strip(), "provenance": PROVENANCE, "current_settings": base,
                "default_values_with_sources": [{"item": i, "default": v, "source": src} for i, v, src in SOURCES],
                "parameters": {k: {"range_or_choices": v[1] if isinstance(v[1], list) else [v[1], v[2]],
                                   "description": v[3]} for k, v in PARAMS.items()}}
    if name == "search_docs":
        return search_docs(str(args.get("query", "")))
    raise ValueError(f"Unknown tool {name}")


def ask(client, question, history, base, base_data):
    """Answer one question. history: prior [{'q', 'a'}] pairs (text only).
    Returns {'answer': str, 'calls': [{'tool', 'input', 'output' | 'error'}]}."""
    messages = []
    for h in history[-3:]:
        messages += [{"role": "user", "content": h["q"]}, {"role": "assistant", "content": h["a"]}]
    messages.append({"role": "user", "content": question})
    calls = []
    for _ in range(MAX_TOOL_CALLS + 2):
        resp = client.messages.create(
            model=MODEL, max_tokens=MAX_TOKENS, system=SYSTEM, tools=TOOLS, messages=messages,
            thinking={"type": "between_tools"},  # no long reasoning: keeps answers inside ~1000 tokens
            tool_choice={"type": "auto"} if len(calls) < MAX_TOOL_CALLS else {"type": "none"},
            cache_control={"type": "ephemeral"},
        )
        text = "".join(b.text for b in resp.content if b.type == "text").strip()
        if resp.stop_reason == "refusal":
            return {"answer": "The assistant declined to answer this question.", "calls": calls}
        if resp.stop_reason != "tool_use":
            if resp.stop_reason == "max_tokens":
                text += "\n\n_(Answer cut off at the length limit.)_"
            return {"answer": text or "No answer was produced.", "calls": calls}
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for b in resp.content:
            if b.type != "tool_use":
                continue
            if len(calls) >= MAX_TOOL_CALLS:
                out, err = f"Tool call limit ({MAX_TOOL_CALLS}) reached. Answer with the results you have.", True
            else:
                try:
                    out, err = run_tool(b.name, b.input, base, base_data), False
                    calls.append({"tool": b.name, "input": b.input, "output": out})
                except Exception as e:  # bad parameters go back to the model to fix
                    out, err = str(e), True
                    calls.append({"tool": b.name, "input": b.input, "error": out})
            results.append({"type": "tool_result", "tool_use_id": b.id, "is_error": err,
                            "content": out if err else json.dumps(out, default=str)})
        messages.append({"role": "user", "content": results})
    return {"answer": "Stopped after too many steps without a final answer.", "calls": calls}
