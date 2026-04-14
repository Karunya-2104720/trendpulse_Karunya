import pandas as pd
import os

# Step 1: Find JSON file
data_folder = "data"
files = os.listdir(data_folder)

json_file = None
for file in files:
    if file.endswith(".json"):
        json_file = os.path.join(data_folder, file)
        break

if not json_file:
    print("No JSON file found!")
    exit()

# Load JSON into DataFrame
df = pd.read_json(json_file)

print(f"Loaded {len(df)} stories from {json_file}")

# Step 2: Clean Data

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Clean whitespace in title
df["title"] = df["title"].str.strip()

# Step 3: Save CSV
output_file = os.path.join(data_folder, "trends_clean.csv")
df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Summary: stories per category
print("\nStories per category:")
print(df["category"].value_counts())