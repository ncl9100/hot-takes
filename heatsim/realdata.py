"""Real metered load shape: summed hourly steam for 7 dorms ("Lodging/residential") at the
Cockatoo site in Building Data Genome 2 (Miller et al., Sci Data 7, 368, 2020; CC BY-SA),
with that site's air temperature. Built by scripts/real_data_validation.py.

This is dorm steam (space heating plus hot water), NOT metered NYCHA data. The app uses
only its shape, rescaled to the chosen average demand.
"""
from pathlib import Path
import numpy as np
import pandas as pd

PATH = Path(__file__).resolve().parents[1] / "data" / "real_demand_cockatoo.csv"
SIM_YEAR = 2017  # simulated year; earlier rows only train the forecast


def available():
    return PATH.exists()


def load(avg_source_mw=1.0):
    """Returns (weather for SIM_YEAR, demand for SIM_YEAR, demand all years, temp all years,
    observed mask all years). Demand is source-side MW with SIM_YEAR mean = avg_source_mw
    (ASSUMPTION: the dorm shape scales linearly to our network's size)."""
    df = pd.read_csv(PATH, parse_dates=["timestamp"], index_col="timestamp").asfreq("h")
    sim = df.index.year == SIM_YEAR
    demand_all = (df["steam_meter"] * avg_source_mw / df.loc[sim, "steam_meter"].mean()).rename("demand_mw")
    observed = df["filled"].values == 0
    weather = df.loc[sim, ["temp_c"]]
    return weather, demand_all[sim], demand_all, df["temp_c"], np.asarray(observed)
