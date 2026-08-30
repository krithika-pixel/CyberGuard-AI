print("script started")

import pandas as pd
import numpy as np

df = pd.read_parquet(
    r"dataset/CIC-IDS2017/Infiltration-Thursday-no-metadata.parquet"
)

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nLabels:")
print(df["Label"].value_counts())


print("\nLabel distribution:")
print(df["Label"].value_counts())

print("\nUnique labels:")
print(df["Label"].unique())