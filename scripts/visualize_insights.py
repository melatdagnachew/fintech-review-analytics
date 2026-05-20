import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/sentiment_reviews.csv")

# ==============================
# 1. SENTIMENT DISTRIBUTION
# ==============================

sentiment_counts = pd.crosstab(
    df["bank"],
    df["sentiment_label"]
)

sentiment_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.tight_layout()

plt.savefig("data/raw/sentiment_distribution.png")
plt.close()

# ==============================
# 2. RATING DISTRIBUTION
# ==============================

plt.figure(figsize=(8, 5))

for bank in df["bank"].unique():
    subset = df[df["bank"] == bank]
    plt.hist(
        subset["rating"],
        bins=5,
        alpha=0.5,
        label=bank
    )

plt.title("Rating Distribution per Bank")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()

plt.savefig("data/raw/rating_distribution.png")
plt.close()

# ==============================
# 3. TOP WORDS
# ==============================

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(
    stop_words="english",
    max_features=10
)

X = vectorizer.fit_transform(df["review"].astype(str))

words = vectorizer.get_feature_names_out()
counts = X.sum(axis=0).A1

word_df = pd.DataFrame({
    "word": words,
    "count": counts
})

word_df = word_df.sort_values(
    by="count",
    ascending=True
)

plt.figure(figsize=(8, 5))

plt.barh(
    word_df["word"],
    word_df["count"]
)

plt.title("Top Keywords in Reviews")
plt.xlabel("Frequency")
plt.ylabel("Keyword")
plt.tight_layout()

plt.savefig("data/raw/top_keywords.png")
plt.close()

print("Visualizations created successfully.")
