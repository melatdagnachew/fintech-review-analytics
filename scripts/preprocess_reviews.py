import pandas as pd

# Load raw data
df = pd.read_csv("/Users/melatdagnachew/Downloads/10 acadamy/data/raw/raw_reviews.csv")

print("Before cleaning:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Drop rows missing critical values
df = df.dropna(subset=["review", "rating"])

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

print("After cleaning:", df.shape)

# Save cleaned dataset
df.to_csv("clean_reviews.csv", index=False)

print("Clean dataset saved to data/raw/clean_reviews.csv")
