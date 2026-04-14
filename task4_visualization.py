import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
file_path = "data/trends_analysed.csv"

if not os.path.exists(file_path):
    print("File not found!")
    exit()

df = pd.read_csv(file_path)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Chart 1: Top 10 stories by score
# -----------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -----------------------------
# Chart 2: Stories per category
# -----------------------------
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()

# -----------------------------
# Chart 3: Score vs Comments
# -----------------------------
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -----------------------------
# BONUS: Dashboard
# -----------------------------
fig, axs = plt.subplots(2, 2)

# Chart 1
axs[0, 0].barh(top10["title"], top10["score"])
axs[0, 0].set_title("Top 10 Stories")
axs[0, 0].invert_yaxis()

# Chart 2
axs[0, 1].bar(category_counts.index, category_counts.values)
axs[0, 1].set_title("Categories")

# Chart 3
axs[1, 0].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[1, 0].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[1, 0].set_title("Score vs Comments")
axs[1, 0].legend()

# Hide empty subplot
axs[1, 1].axis("off")

fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in 'outputs/' folder ✅")