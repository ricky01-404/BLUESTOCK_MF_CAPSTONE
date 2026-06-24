import pandas as pd
import os

INPUT_FILE = "data/raw/08_investor_transactions.csv"
OUTPUT_FILE = "data/processed/clean_transactions.csv"

os.makedirs("data/processed", exist_ok=True)

print("Loading transaction data...")

df = pd.read_csv(INPUT_FILE)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP"
})

# Validate transaction types
valid_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

invalid_types = (
    ~df["transaction_type"]
    .isin(valid_types)
).sum()

print(f"Invalid transaction types: {invalid_types}")

# Validate amount
invalid_amounts = (
    df["amount_inr"] <= 0
).sum()

print(f"Invalid amounts: {invalid_amounts}")

df = df[df["amount_inr"] > 0]

# Validate KYC
valid_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = (
    ~df["kyc_status"]
    .isin(valid_kyc)
).sum()

print(f"Invalid KYC values: {invalid_kyc}")

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"Duplicates removed: {before - after}")

# Save
df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSaved:")
print(OUTPUT_FILE)

print("\nFinal Shape:")
print(df.shape)