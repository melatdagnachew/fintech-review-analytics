import pandas as pd
from transformers import pipeline

# Load data
df = pd.read_csv("/Users/melatdagnachew/Downloads/10 acadamy/fintech-review-analytics/fintech-review-analytics/scripts/clean_reviews.csv")

# Initialize transformer sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def get_sentiment(text):
    try:
        result = sentiment_pipeline(str(text))[0]
        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            return "positive", score
        else:
            return "negative", score
    except:
        return "neutral", 0.0


labels = []
scores = []

for review in df["review"]:
    label, score = get_sentiment(review)
    labels.append(label)
    scores.append(score)

df["sentiment_label"] = labels
df["sentiment_score"] = scores

# Aggregate analysis
print(df.groupby("bank")["sentiment_score"].mean())
print(df.groupby(["bank", "rating"])["sentiment_score"].mean())

# Save output
df.to_csv("/Users/melatdagnachew/Downloads/10 acadamy/fintech-review-analytics/fintech-review-analytics/data/raw/sentiment_reviews.csv", index=False)

print("Sentiment analysis complete")
