"""Test heatsim's day-ahead demand forecast on real metered steam data.

Data: Building Data Genome 2 (BDG2), the open release of Kaggle's ASHRAE Great Energy
Predictor III, github.com/buds-lab/building-data-genome-project-2 (license: CC BY-SA, see that repo's LICENSE file).
Hourly steam meters on "Lodging/residential" (dorm) buildings at US Eastern-time sites.
Trained on 2016, tested day-ahead on 2017.

Run from the repo root:  .venv\\Scripts\\python scripts/real_data_validation.py
Raw files are downloaded once into data/raw/ (gitignored, never committed).
Writes data/real_steam_results.csv.
"""
import sys
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from heatsim.forecast import features, profile_forecast  # noqa: E402

RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "real_steam_results.csv"
BASE = "https://media.githubusercontent.com/media/buds-lab/building-data-genome-project-2/master/data/"
FILES = {
    "steam_cleaned.csv": "meters/cleaned/steam_cleaned.csv",
    "weather.csv": "weather/weather.csv",
    "metadata.csv": "metadata/metadata.csv",
}


def download():
    RAW.mkdir(parents=True, exist_ok=True)
    for name, path in FILES.items():
        dest = RAW / name
        if dest.exists():
            continue
        print("Downloading", BASE + path)
        tmp = dest.with_suffix(".part")
        urllib.request.urlretrieve(BASE + path, tmp)
        tmp.replace(dest)


download()
steam = pd.read_csv(RAW / "steam_cleaned.csv", parse_dates=["timestamp"], index_col="timestamp")
wx = pd.read_csv(RAW / "weather.csv", parse_dates=["timestamp"])
meta = pd.read_csv(RAW / "metadata.csv")


def metrics(y, p):
    y, p = np.asarray(y), np.asarray(p); ok = ~np.isnan(p)
    y, p = y[ok], p[ok]
    wape = np.abs(p-y).sum()/y.sum()
    m = y > 0.1*y.mean()
    mape = np.mean(np.abs(p[m]-y[m])/y[m])
    return wape, mape


rows = []


def run(name, d, temp):
    d = d.asfreq("h").interpolate(limit=6); temp = temp.reindex(d.index).interpolate(limit=12).ffill().bfill()
    ok = d.notna()
    tr = d.index.year == 2016; te = d.index.year == 2017
    X = features(d, temp)
    mtr = tr & ok.values
    model = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=0).fit(X[mtr], d[mtr])
    dte = d[te]; Xte = X[te]; keep = dte.notna().values
    pred = model.predict(Xte)[keep]; y = dte.values[keep]
    pers = d.shift(24)[te].values[keep]
    prof = profile_forecast(d.ffill())[te].values[keep]
    r = {"series": name, "hours_tested": int(keep.sum()), "mean_load": float(y.mean())}
    for k, p in [("ml", pred), ("profile", prof), ("persistence", pers)]:
        r[k+"_wape"], r[k+"_mape"] = metrics(y, p)
    rows.append(r)


for site in ["Cockatoo", "Peacock", "Eagle"]:
    ids = meta[(meta.site_id == site) & meta.primaryspaceusage.str.contains("Lodging", na=False) & meta.steam.notna()].building_id
    cols = [c for c in ids if c in steam.columns]
    good = [c for c in cols if steam[c].notna().mean() > 0.9 and (steam[c] > 0).mean() > 0.8]
    temp = wx[wx.site_id == site].set_index("timestamp")["airTemperature"]
    temp = temp[~temp.index.duplicated()]
    run(f"{site} all lodging ({len(good)} bldgs summed)", steam[good].sum(axis=1, min_count=len(good)), temp)
    for c in good: run(c, steam[c], temp)
    print(site, len(cols), "meters,", len(good), "usable")
df = pd.DataFrame(rows)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 20)
print(df.round(3).to_string())
ind = df[~df.series.str.contains("summed")]
print("\nIndividual buildings, median:", ind[["ml_wape","profile_wape","persistence_wape","ml_mape","profile_mape","persistence_mape"]].median().round(3).to_dict())
print("ML beats profile (WAPE) in", (ind.ml_wape < ind.profile_wape).sum(), "of", len(ind))
df.to_csv(OUT, index=False)
print("Wrote", OUT)
