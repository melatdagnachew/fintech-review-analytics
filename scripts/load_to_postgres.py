import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="melatdagnachew",
    password="",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert bank metadata
banks = [
    ("CBE", "Commercial Bank of Ethiopia Mobile"),
    ("BOA", "Bank of Abyssinia Mobile"),
    ("Dashen", "Dashen Super App")
]

for bank_name, app_name in banks:
    cur.execute(
        """
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        """,
        (bank_name, app_name)
    )

conn.commit()

# Fetch bank IDs
cur.execute("SELECT bank_id, bank_name FROM banks")
bank_map = {name: bank_id for bank_id, name in cur.fetchall()}

# Load CSV
df = pd.read_csv("data/raw/sentiment_reviews.csv")

# Insert reviews
for _, row in df.iterrows():

    cur.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            bank_map.get(row["bank"]),
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["source"]
        )
    )

conn.commit()

print("Data inserted successfully.")

cur.close()
conn.close()
