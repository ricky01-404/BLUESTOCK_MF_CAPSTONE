import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():
    try:
        print(f"Fetching {name}...")

        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            filename = f"data/raw/{name}_nav.csv"
            nav_df.to_csv(filename, index=False)

            print(f"Saved: {filename}")

        else:
            print(f"Failed: {code}")

    except Exception as e:
        print(f"Error fetching {name}: {e}")

print("\nAll NAV files processed.")