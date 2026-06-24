import pandas as pd
import os

INPUT_FILE = "data/raw/02_nav_history.csv"
OUTPUT_FILE = "data/processed/clean_nav_history.csv"

os.makedirs("data/processed", exist_ok=True)

print("Loading NAV data...")

df = pd.read_csv(INPUT_FILE)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort records
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"Duplicates removed: {before - after}")

# Validate NAV > 0
invalid_nav = (df["nav"] <= 0).sum()

print(f"Invalid NAV rows: {invalid_nav}")

df = df[df["nav"] > 0]

# Forward fill NAV per fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Save
df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSaved:")
print(OUTPUT_FILE)

print("\nFinal Shape:")
print(df.shape)