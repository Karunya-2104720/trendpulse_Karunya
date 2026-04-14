import pandas as pd
import numpy as np
import os

# Load CSV
file_path = "data/trends_clean.csv"

if not os.path.exists(file_path):
    print("CSV file not found!")
    exit()

df = pd.read_csv(file_path)

# --- Load and Explore ---
print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score: {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# --- NumPy Analysis ---
scores = df["score"].values

print("\n--- NumPy Stats ---")
print(f"Mean score: {np.mean(scores):.2f}")
print(f"Median score: {np.median(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")
print(f"Max score: {np.max(scores)}")
print(f"Min score: {np.min(scores)}")

# Most common category
top_category = df["category"].value_counts().idxmax()
count_top = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({count_top} stories)")

# --- Add New Columns ---

# Engagement
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular
df["is_popular"] = df["score"] > avg_score

# --- Save Result ---
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved analysed data to {output_file}")