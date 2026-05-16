import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("/Users/melatdagnachew/Downloads/10 acadamy/fintech-review-analytics/fintech-review-analytics/data/raw/sentiment_reviews.csv")

# Basic text cleaning is assumed already done

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    max_features=50
)

X = vectorizer.fit_transform(df["review"].astype(str))

terms = vectorizer.get_feature_names_out()

# Simple keyword grouping logic (baseline themes)
def assign_theme(text):
    text = str(text).lower()

    if any(word in text for word in ["login", "password", "otp", "sign"]):
        return "Account Access Issues"

    if any(word in text for word in ["slow", "lag", "load", "transfer"]):
        return "Transaction Performance"

    if any(word in text for word in ["ui", "design", "interface"]):
        return "UI & Design"

    if any(word in text for word in ["error", "crash", "bug"]):
        return "App Stability"

    if any(word in text for word in ["feature", "add", "request"]):
        return "Feature Requests"

    return "Other"


df["theme"] = df["review"].apply(assign_theme)

# Save final output
df.to_csv("/Users/melatdagnachew/Downloads/10 acadamy/fintech-review-analytics/fintech-review-analytics/data/raw/themed_reviews.csv", index=False)

print(df["theme"].value_counts())
print("Theme analysis complete")
