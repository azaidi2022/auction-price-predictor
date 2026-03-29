import pandas as pd


def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Parse sale date
    df["saledate_dt"] = pd.to_datetime(df["saledate"], errors="coerce", utc=True)
    df["saledate_dt"] = df["saledate_dt"].dt.tz_localize(None)

    # Date features
    df["sale_month"] = df["saledate_dt"].dt.month
    df["sale_dow"] = df["saledate_dt"].dt.dayofweek
    df["sale_year"] = df["saledate_dt"].dt.year

    # Vehicle age
    df["vehicle_age"] = df["sale_year"] - df["year"]

    # Mileage bucket
    df["mileage_bucket"] = pd.cut(
        df["odometer"],
        bins=[0, 30000, 60000, 100000, 150000, 1000000],
        labels=["0-30k", "30-60k", "60-100k", "100-150k", "150k+"]
    )

    # Condition bucket
    df["condition_bucket"] = pd.cut(
        df["condition"],
        bins=[0, 2.5, 3.5, 4.5, 6],
        labels=["Poor", "Fair", "Good", "Excellent"]
    )

    # Region grouping
    region_map = {
        "TX": "South", "FL": "South", "GA": "South", "NC": "South", "SC": "South",
        "AL": "South", "TN": "South", "LA": "South", "MS": "South", "AR": "South",
        "NY": "Northeast", "NJ": "Northeast", "PA": "Northeast", "MA": "Northeast",
        "CT": "Northeast", "RI": "Northeast", "NH": "Northeast", "VT": "Northeast",
        "ME": "Northeast",
        "IL": "Midwest", "OH": "Midwest", "MI": "Midwest", "IN": "Midwest",
        "WI": "Midwest", "MN": "Midwest", "MO": "Midwest", "IA": "Midwest",
        "KS": "Midwest",
        "CA": "West", "WA": "West", "OR": "West", "NV": "West", "AZ": "West",
        "CO": "West", "UT": "West", "NM": "West", "ID": "West", "MT": "West"
    }
    df["region_group"] = df["state"].map(region_map).fillna("Other")

    return df
