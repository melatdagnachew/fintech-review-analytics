# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian fintech mobile banking applications on the Google Play Store.

The goal is to collect, clean, and prepare user reviews for sentiment analysis, thematic analysis, database storage, and business recommendations.

The three banks analyzed are:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

## Task 1: Data Collection and Preprocessing

### Objective

Scrape user reviews from the Google Play Store and preprocess them into a clean, analysis-ready dataset.

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- google-play-scraper
- Git & GitHub
- GitHub Actions (CI/CD)

---

## Data Collection Methodology

Reviews were collected using the `google-play-scraper` Python library from the Google Play Store.

The following fields were collected:

- Review Text
- Rating (1–5 stars)
- Review Date
- Bank Name
- Source (Google Play)

Each bank was targeted for a minimum of 400 reviews.

### Apps Scraped

| Bank | Source |
|---|---|
| CBE | Google Play |
| BOA | Google Play |
| Dashen | Google Play |

### Date Range

Reviews were collected using the latest available reviews returned by the scraper using `Sort.NEWEST`.

---

## Data Preprocessing Steps

The following preprocessing steps were applied:

1. Removed duplicate reviews
2. Dropped rows with missing review text
3. Dropped rows with missing ratings
4. Standardized review dates to YYYY-MM-DD format
5. Saved final clean dataset as CSV

Final dataset columns:

- review
- rating
- date
- bank
- source

---

## Limitations Encountered

Some applications may return fewer reviews than expected due to:

- Google Play Store API limitations
- Regional restrictions
- Review availability constraints
- Language filtering limitations

If fewer than 400 reviews were returned for a bank, this was documented and the broader available review range was used.

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
