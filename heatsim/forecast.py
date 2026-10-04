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


def profile_forecast(demand, window=28):
    """Non-ML baseline: mean of the same hour and day type (weekday/weekend) over the
    previous `window` occurrences. Uses only data at least 24 h old, so it is day-ahead."""
    idx = demand.index
    key = idx.hour + 24 * (idx.dayofweek >= 5)
    out = demand.groupby(key).transform(lambda s: s.shift(1).rolling(window, min_periods=1).mean())
    return out.bfill().rename("profile_mw")


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
    profile = profile_forecast(test_demand)
    return pred, profile, _errors(y, pred.values, persist, profile.values)


def _errors(y, ml, persist, profile, mape_min=0.0):
    """Forecast errors. MAPE skips hours with y <= mape_min, where it is undefined or explodes."""
    m = y > mape_min
    mape = lambda p: float(np.mean(np.abs(p[m] - y[m]) / y[m]))
    return {
        "ml_mape": mape(ml),
        "persistence_mape": mape(persist),
        "profile_mape": mape(profile),
        "ml_mae_mw": float(np.mean(np.abs(ml - y))),
        "ml_wape": float(np.abs(ml - y).sum() / y.sum()),
        "persistence_wape": float(np.abs(persist - y).sum() / y.sum()),
        "profile_wape": float(np.abs(profile - y).sum() / y.sum()),
    }


def train_and_forecast_real(demand, temp, observed, test_year=2017):
    """Real metered load: train on the years before test_year (observed hours only) and
    forecast test_year a day ahead. demand/temp cover all years; gap-filled hours are
    used for lag features but excluded from training and from the error metrics."""
    X = features(demand, temp)
    test = demand.index.year == test_year
    train = (demand.index.year < test_year) & observed
    model = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=0)
    model.fit(X[train], demand[train])
    pred = pd.Series(model.predict(X[test]), index=demand.index[test], name="forecast_mw")
    profile = profile_forecast(demand)[test]
    persist = demand.shift(24)[test]
    ok = observed[test]
    y = demand[test].values[ok]
    # MAPE skips hours under 10% of mean load, as in scripts/real_data_validation.py; WAPE uses all hours
    return pred, profile, _errors(y, pred.values[ok], persist.values[ok], profile.values[ok], mape_min=0.1 * y.mean())


def forward_sum(x, hours):
    """Sum of x over the next `hours` hours (including now)."""
    s = pd.Series(np.asarray(x, float))
    return s[::-1].rolling(hours, min_periods=1).sum()[::-1].values


POLICY_NAMES = ["Fixed worst case (no forecast)", "ML forecast", "Hour-of-day profile (no ML)",
                "Perfect foresight (upper bound)", "No reserve"]


def reserve_policies(demand, forecast, profile, ride_through_h=8, margin=0.10):
    """Ways to decide how much energy to hold back for outages (MWh, before the
    simulation caps it at storage capacity). margin is an ASSUMPTION safety factor."""
    n = len(demand)
    return dict(zip(POLICY_NAMES, [
        np.full(n, ride_through_h * np.percentile(demand, 99)),
        forward_sum(forecast, ride_through_h) * (1 + margin),
        forward_sum(profile, ride_through_h) * (1 + margin),
        forward_sum(demand, ride_through_h),
        np.zeros(n),
    ]))
