import json
import csv
import os

# Ensure data folder exists
data_folder = "data"

# Find JSON file
files = os.listdir(data_folder)
json_file = None

for file in files:
    if file.endswith(".json"):
        json_file = os.path.join(data_folder, file)
        break

if not json_file:
    print("No JSON file found!")
    exit()

print(f"Using file: {json_file}")

# Load JSON
with open(json_file, "r") as f:
    data = json.load(f)

cleaned_data = []

for item in data:
    # Clean fields
    cleaned_item = {
        "post_id": item.get("post_id", ""),
        "title": item.get("title", "").strip(),
        "category": item.get("category", ""),
        "score": item.get("score", 0),
        "num_comments": item.get("num_comments", 0),
        "author": item.get("author", ""),
        "collected_at": item.get("collected_at", "")
    }

    # Skip empty titles
    if cleaned_item["title"] == "":
        continue

    cleaned_data.append(cleaned_item)

# Save CSV
output_file = os.path.join(data_folder, "trends_cleaned.csv")

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned_data[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_data)

print("Cleaning complete ✅")
print(f"Saved to: {output_file}")
print(f"Total records: {len(cleaned_data)}")