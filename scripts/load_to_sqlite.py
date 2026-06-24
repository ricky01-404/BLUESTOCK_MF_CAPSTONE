import pandas as pd
from sqlalchemy import create_engine
import os

# Create database folder
os.makedirs("data/db", exist_ok=True)

# SQLite database
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

print("Loading datasets...")

# =====================================================
# LOAD DATA
# =====================================================

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

transactions = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# =====================================================
# CREATE DATE DIMENSION
# =====================================================

nav["date"] = pd.to_datetime(nav["date"])

date_dim = pd.DataFrame({
    "full_date": sorted(nav["date"].unique())
})

date_dim["year"] = date_dim["full_date"].dt.year
date_dim["quarter"] = date_dim["full_date"].dt.quarter
date_dim["month"] = date_dim["full_date"].dt.month
date_dim["day"] = date_dim["full_date"].dt.day
date_dim["weekday"] = date_dim["full_date"].dt.weekday

date_dim.insert(0, "date_id", range(1, len(date_dim)+1))

# =====================================================
# LOAD TABLES
# =====================================================

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

date_dim.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("\nDatabase Loaded Successfully!")

print("\nRow Counts")
print("----------------------")
print("dim_fund:", len(fund))
print("dim_date:", len(date_dim))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))
print("fact_aum:", len(aum))