import pandas as pd
from catboost import CatBoostRegressor
from src.preprocess import preprocess_input

FEATURES = [
    "year",
    "vehicle_age",
    "make",
    "model",
    "trim",
    "body",
    "transmission",
    "state",
    "region_group",
    "odometer",
    "mileage_bucket",
    "condition",
    "condition_bucket",
    "color",
    "interior",
    "sale_month",
    "sale_dow",
]

model = CatBoostRegressor()
model.load_model("model/catboost_dollar_spread.cbm")


def predict_spread(payload: dict) -> float:
    df = pd.DataFrame([payload])
    df = preprocess_input(df)

    X = df[FEATURES].copy()

    cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

    for c in cat_cols:
        X[c] = X[c].astype("string").fillna("Unknown")

    num_cols = [c for c in X.columns if c not in cat_cols]
    for c in num_cols:
        X[c] = pd.to_numeric(X[c], errors="coerce")
        X[c] = X[c].fillna(0)

    pred = model.predict(X)[0]
    return float(pred)
