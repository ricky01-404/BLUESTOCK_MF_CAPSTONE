import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Total fund codes: {len(master_codes)}")
print(f"Codes found in NAV history: {len(master_codes) - len(missing_codes)}")
print(f"Missing codes: {len(missing_codes)}")

if missing_codes:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes validated successfully.")