import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

processed_frames = []

for csv_file in DATA_DIR.glob("daily_sales_data_*.csv"):
    df = pd.read_csv(csv_file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns as specified
    df = df.rename(columns={
        "date": "Date",
        "region": "Region"
    })

    processed_frames.append(df)

final_df = pd.concat(processed_frames, ignore_index=True)

final_df.to_csv("formatted_sales.csv", index=False)

print("formatted_sales.csv created successfully")
