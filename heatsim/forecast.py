"""ML component: day-ahead heat demand forecasting that sets the storage reserve.

Problem it solves: the brief counts the same 12 MWh for peak shaving AND 8 h of
outage ride-through. A fixed worst-case reserve locks the battery so it can't shave
peaks. A forecast-based reserve holds only what the next H hours actually need.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from .model import synth_weather, synth_demand


def features(demand, temp):
    idx = demand.index
    X = pd.DataFrame({
        "hour": idx.hour, "dow": idx.dayofweek, "doy": idx.dayofyear,
        "temp": temp.values,
        "temp_24h_mean": temp.rolling(24, min_periods=1).mean().values,
        "lag_24h": demand.shift(24).values,     # known at forecast time (day-ahead)
        "lag_168h": demand.shift(168).values,
    }, index=idx)
    return X


def train_and_forecast(test_demand, test_weather, avg_source_mw=1.0, space_heat_share=0.0,
                       peak_ratio=1.64, n_train_years=3):
    """Train on independent synthetic years, evaluate on the simulation year.
    Swap the training data for real metered data (see README)."""
    Xs, ys = [], []
    for k in range(n_train_years):
        w = synth_weather(seed=100 + k)
        d = synth_demand(w, avg_source_mw, peak_ratio, space_heat_share, seed=200 + k)
        Xs.append(features(d, w["temp_c"]))
        ys.append(d.values)
    model = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=0)
    model.fit(pd.concat(Xs), np.concatenate(ys))
    Xt = features(test_demand, test_weather["temp_c"])
    pred = pd.Series(model.predict(Xt), index=test_demand.index, name="forecast_mw")
    y = test_demand.values
    persist = test_demand.shift(24).bfill().values
    metrics = {
        "ml_mape": float(np.mean(np.abs(pred.values - y) / y)),
        "persistence_mape": float(np.mean(np.abs(persist - y) / y)),
        "ml_mae_mw": float(np.mean(np.abs(pred.values - y))),
    }
    return pred, metrics


def forward_sum(x, hours):
    """Sum of x over the next `hours` hours (including now)."""
    s = pd.Series(np.asarray(x, float))
    return s[::-1].rolling(hours, min_periods=1).sum()[::-1].values


def reserve_policies(demand, forecast, ride_through_h=8, margin=0.10):
    """Three ways to decide how much energy to hold back for outages."""
    return {
        "Fixed worst case (no forecast)": np.full(len(demand), ride_through_h * np.percentile(demand, 99)),
        "ML forecast": forward_sum(forecast, ride_through_h) * (1 + margin),
        "Perfect foresight (upper bound)": forward_sum(demand, ride_through_h),
        "No reserve": np.zeros(len(demand)),
    }
