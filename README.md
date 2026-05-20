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
```
## Task 2: Sentiment and Thematic Analysis

## Objective

The goal of this task is to quantify customer sentiment and identify recurring themes from Google Play Store reviews for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

This helps uncover customer satisfaction drivers, major frustrations, and product improvement opportunities.

---

## Sentiment Analysis

We used the transformer model:

`distilbert-base-uncased-finetuned-sst-2-english`

This model was selected because it provides stronger contextual understanding compared to lexicon-based tools like VADER and TextBlob.

Each review was classified into:

- Positive
- Negative
- Neutral (fallback case)

Each prediction includes:

- sentiment label
- confidence score

Sentiment scores were also aggregated by:

- Bank
- Star rating

This helps compare customer satisfaction across institutions.

---

## Thematic Analysis

TF-IDF with unigram and bigram extraction was used to identify recurring keywords and significant phrases.

Examples include:

- login error
- slow transfer
- OTP not received
- app crash
- fingerprint login

These keywords were grouped manually into business-relevant themes.

---

## Theme Grouping Logic

### 1. Account Access Issues

Keywords:

- login
- password
- OTP
- verification
- sign in

This theme captures failed authentication and account access problems.

---

### 2. Transaction Performance

Keywords:

- transfer
- slow
- transaction
- delay
- loading

This theme reflects issues affecting payment speed and reliability.

---

### 3. UI & Design

Keywords:

- UI
- design
- interface
- layout

This theme includes usability and visual experience feedback.

---

### 4. App Stability

Keywords:

- crash
- error
- bug
- freeze

This theme captures technical failures affecting trust and retention.

---

### 5. Feature Requests

Keywords:

- fingerprint login
- budgeting tools
- add feature
- request

This theme captures customer requests for new functionality and competitive improvements.

# Task 3: PostgreSQL Database Engineering

## Database Setup

PostgreSQL was installed locally and a database named `bank_reviews` was created.

---

## Schema Design

Two relational tables were created:

### banks

Stores metadata about each banking application.

Columns:

- bank_id
- bank_name
- app_name

### reviews

Stores cleaned and processed review data.

Columns:

- review_id
- bank_id
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- source

---

## Data Insertion

Python with `psycopg2` was used to insert processed review data into PostgreSQL.

A total of 1,477 reviews were inserted successfully.

---

## Verification Queries

SQL queries were executed to verify:

- review counts per bank
- average ratings per bank
- absence of null values in key columns

Results confirmed successful insertion and strong data quality.

# Final Insights and Recommendations

## Overview

This analysis examined Google Play Store reviews for:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal was to identify customer satisfaction drivers, recurring pain points, and actionable product recommendations.

---

# 1. Comparative Analysis

## Average Ratings

| Bank | Average Rating |
|------|------|
| CBE | 4.10 |
| Dashen | 3.92 |
| BOA | 3.56 |

CBE showed the strongest overall customer satisfaction while BOA recorded the lowest average rating.

---

# 2. Satisfaction Drivers

## CBE

### Drivers

- Reliable transaction experience in many positive reviews
- Strong overall trust and familiarity among users

### Pain Points

- Slow transfers during peak usage
- Login and OTP issues reported repeatedly

---

## BOA

### Drivers

- Some users praised app functionality and convenience
- Positive feedback around banking accessibility

### Pain Points

- Frequent authentication and OTP failures
- Higher concentration of negative sentiment

---

## Dashen

### Drivers

- Positive feedback about UI and usability
- Customers appreciated modern interface design

### Pain Points

- App crashes and stability complaints
- Requests for additional features and improvements

---

# 3. Dominant Themes

The most common themes identified across all banks were:

- Account Access Issues
- Transaction Performance
- App Stability
- UI & Design
- Feature Requests

Transaction delays and authentication failures appeared consistently across institutions.

---

# 4. Recommendations

## CBE

### Recommendations

1. Optimize backend transfer performance during high traffic periods
2. Improve OTP reliability and login recovery flows

---

## BOA

### Recommendations

1. Prioritize authentication stability and error handling
2. Improve customer support response for failed login cases

---

## Dashen

### Recommendations

1. Focus on crash reduction and app stability improvements
2. Expand modern features such as biometric login and budgeting tools

---

# 5. Ethical Considerations

Several potential biases may affect interpretation of review data:

- Negativity bias: users are more likely to leave reviews after poor experiences
- Sampling bias: scraped reviews may overrepresent recent customer experiences
- Language bias: multilingual reviews may reduce NLP accuracy

These limitations should be considered when translating insights into product strategy.

---

# 6. Conclusion

The analysis demonstrates that customer reviews provide valuable operational and competitive intelligence for Ethiopian fintech applications.

Across all three banks, users consistently emphasized transaction reliability, authentication performance, and application stability as critical drivers of customer satisfaction and retention.

The findings can help prioritize product improvements, reduce customer frustration, and improve digital banking competitiveness.
