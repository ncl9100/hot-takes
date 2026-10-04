"""Financial, customer, carbon and water model. Defaults from the team brief."""
from dataclasses import dataclass
import numpy as np
from .model import MMBTU_PER_MWH

KWH_PER_MMBTU = 293.071


@dataclass
class FinanceInputs:
    capture_base_cost: float = 2.5e6     # brief: $2.5M for 1.5 MW capture
    capture_base_mw: float = 1.5
    capture_scale_exp: float = 0.6       # ASSUMPTION: equipment cost scales sublinearly
    storage_cost_per_kwh: float = 120.0  # brief: $80-150/kWh installed PCM
    pipe_ft: float = 1200.0
    pipe_cost_per_ft: float = 6000.0
    connections: float = 1.0e6
    soft_pct: float = 0.25
    itc_pct: float = 0.30                # 48E base ITC on storage
    ratepayer_share: float = 0.0         # share of capex recovered via utility rates
    discount: float = 0.06
    years: int = 30
    om_pct: float = 0.02
    heat_price: float = 15.0             # $/MMBtu source heat, NYCHA affordable rate
    commercial_share: float = 0.0        # share of heat sold at commercial rate (LL97 buyers)
    commercial_price: float = 35.0       # ASSUMPTION
    steam_price: float = 40.0            # $/MMBtu, Con Ed bill example
    elec_price: float = 0.25             # $/kWh
    cop: float = 3.4
    steam_tco2_per_mmbtu: float = 0.04493   # LL97 2030 steam coefficient
    elec_tco2_per_kwh: float = 0.000145     # LL97 2030 electricity coefficient
    floor_value_per_sqft: float = 28.0
    count_floor_space: bool = False      # off by default: counterfactual tank is debatable
    towers: bool = True                  # cooling towers present -> water savings


def crf(r, n):
    return r * (1 + r) ** n / ((1 + r) ** n - 1)


def capture_cost(mw, f):
    return f.capture_base_cost * (mw / f.capture_base_mw) ** f.capture_scale_exp


def network(summary, capture_mw, storage_mwh, f):
    storage = storage_mwh * 1000 * f.storage_cost_per_kwh
    cap = capture_cost(capture_mw, f)
    pipe = f.pipe_ft * f.pipe_cost_per_ft
    hard = cap + storage + pipe + f.connections
    gross = hard * (1 + f.soft_pct)
    itc = storage * (1 + f.soft_pct) * f.itc_pct
    net = (gross - itc) * (1 - f.ratepayer_share)
    mmbtu = summary["served_by_network_mwh"] * MMBTU_PER_MWH
    price = (1 - f.commercial_share) * f.heat_price + f.commercial_share * f.commercial_price
    revenue = mmbtu * price
    om = gross * f.om_pct
    pv = (revenue - om) / crf(f.discount, f.years)
    lcoh = (net * crf(f.discount, f.years) + om) / mmbtu if mmbtu else np.nan
    cash = [-net] + [revenue - om] * f.years
    cum = np.cumsum(cash)
    payback = next((i for i, c in enumerate(cum) if c >= 0), None)
    return {
        "capex_gross": gross, "itc": itc, "capex_net_to_owner": net,
        "capex_lines": {"Heat capture": cap, "Thermal storage": storage, "Distribution pipe": pipe,
                        "Customer connections": f.connections, "Soft costs": hard * f.soft_pct},
        "heat_sold_mmbtu": mmbtu, "avg_price": price, "revenue": revenue, "om": om,
        "npv": pv - net, "lcoh": lcoh, "payback_years": payback, "cashflow": cash,
        "cost_per_annual_mmbtu": net / mmbtu if mmbtu else np.nan,
    }


def customer(f):
    elec = KWH_PER_MMBTU / f.cop * f.elec_price
    heat = f.heat_price * (f.cop - 1) / f.cop
    total = elec + heat
    return {"electricity": elec, "network_charge": heat, "total": total,
            "steam": f.steam_price, "savings_pct": 1 - total / f.steam_price}


def impact(summary, f):
    src = summary["served_by_network_mwh"] * MMBTU_PER_MWH
    delivered = src * f.cop / (f.cop - 1)
    kwh = delivered * KWH_PER_MMBTU / f.cop
    co2 = delivered * f.steam_tco2_per_mmbtu - kwh * f.elec_tco2_per_kwh
    water = src * 1e6 / 8300 if f.towers else 0.0
    return {"delivered_mmbtu": delivered, "heat_pump_kwh": kwh, "tco2_avoided_vs_steam": co2,
            "water_gal_saved": water}


def storage_value(with_store, without_store, peak_demand_mw, capture_mw, storage_obj, water_obj, f):
    """Incremental value of the storage versus no storage (and optionally a water tank)."""
    storage_capex = storage_obj.capacity_mwh * 1000 * f.storage_cost_per_kwh * (1 + f.soft_pct)
    net = storage_capex * (1 - f.itc_pct)
    avoided_capture = max(0.0, capture_cost(peak_demand_mw, f) - capture_cost(capture_mw, f)) * (1 + f.soft_pct)
    steam_saved = (without_store["steam_mwh"] - with_store["steam_mwh"]) * MMBTU_PER_MWH * f.steam_price
    floor = 0.0
    if f.count_floor_space:
        floor = max(0.0, water_obj.footprint_sqft() - storage_obj.footprint_sqft()) * f.floor_value_per_sqft
    annual = steam_saved + floor
    remaining = net - avoided_capture
    payback = remaining / annual if annual > 0 else np.inf
    return {"storage_capex_net": net, "avoided_capture_capex": avoided_capture,
            "annual_steam_savings": steam_saved, "annual_floor_value": floor,
            "payback_years": max(0.0, payback)}
