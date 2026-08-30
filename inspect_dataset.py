import pandas as pd
import os

DATASET_PATH = "dataset/CIC-IDS2017"

all_data = []

for file in os.listdir(DATASET_PATH):

    if file.endswith(".parquet"):

        path = os.path.join(DATASET_PATH, file)

        df = pd.read_parquet(path)

        print("\n" + "=" * 60)
        print("FILE:", file)
        print("Rows:", len(df))

        print("\nLabels:")
        print(df["Label"].value_counts())

        all_data.append(df)

# Combine everything
data = pd.concat(all_data, ignore_index=True)

print("\n" + "=" * 60)
print("TOTAL DATASET")
print("Rows:", len(data))
print("Columns:", len(data.columns))

print("\nALL LABELS:")
print(data["Label"].value_counts())
