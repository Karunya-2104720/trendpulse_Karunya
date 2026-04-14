import requests
import time
import json
from datetime import datetime
import os

# Start message
print("Starting script...")

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories + keywords
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Assign category
def categorize(title):
    title = title.lower()
    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if word in title:
                return category
    return None

# Fetch top stories
response = requests.get(TOP_STORIES_URL, headers=headers)
story_ids = response.json()[:150]

print("Fetched story IDs")

results = {cat: [] for cat in CATEGORIES}

# Fetch each story
for story_id in story_ids:
    print(f"Processing story {story_id}")
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if not story or "title" not in story:
            continue

        category = categorize(story["title"])

        if category and len(results[category]) < 25:
            results[category].append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().isoformat()
            })

        if all(len(results[c]) >= 25 for c in results):
            break

    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")

# Combine data
final_data = []
for cat in results:
    final_data.extend(results[cat])

# Save file
os.makedirs("data", exist_ok=True)

print("Saving file...")
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(final_data, f, indent=4)

print(f"Collected {len(final_data)} stories. Saved to {filename}")