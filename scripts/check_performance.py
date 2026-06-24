import pandas as pd
import os

INPUT_FILE = "data/raw/07_scheme_performance.csv"
OUTPUT_FILE = "data/processed/clean_performance.csv"

os.makedirs("data/processed", exist_ok=True)

print("Loading performance data...")

df = pd.read_csv(INPUT_FILE)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Expense ratio validation
expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Expense ratio anomalies: {len(expense_anomalies)}")

# Check missing values after numeric conversion
print("\nNull Values:")
print(df[numeric_cols].isnull().sum())

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"\nDuplicates removed: {before - after}")

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nSaved: {OUTPUT_FILE}")
print(f"Final Shape: {df.shape}")