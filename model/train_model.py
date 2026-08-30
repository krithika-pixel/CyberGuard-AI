import pandas as pd

print("Loading dataset...")

df = pd.read_parquet(
    "dataset/CIC-IDS2017/DDoS-Friday-no-metadata.parquet"
)

print("Dataset loaded!")
print("Shape:", df.shape)
print(df.head())

# Separate input features and target
X = df.drop("Label", axis=1)
y = df["Label"]

print("Features shape:", X.shape)
print("Labels shape:", y.shape)


from sklearn.model_selection import train_test_split