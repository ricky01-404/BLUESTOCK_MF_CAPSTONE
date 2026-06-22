import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print(f"FILE: {file}")

    try:
        df = pd.read_csv(os.path.join(DATA_FOLDER, file))

        print(f"\nShape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("\n")