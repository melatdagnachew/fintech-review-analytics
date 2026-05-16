from google_play_scraper import reviews, Sort
import pandas as pd

# App package names
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

print(f"\nTotal reviews collected: {len(df)}")

df.to_csv("raw_reviews.csv", index=False)

print("Saved to data/raw/raw_reviews.csv")
