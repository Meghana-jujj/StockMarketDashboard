import pandas as pd
import sqlite3
import schedule
import time

def compute_trends():
    conn = sqlite3.connect("../database/stocks.db")
    df = pd.read_sql("SELECT * FROM stock_prices", conn)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    trends = df.groupby(["symbol", "date"]).agg({
        "price": ["mean", "std"]
    }).reset_index()
    trends.columns = ["symbol", "date", "avg_price", "price_std"]
    trends.to_sql("daily_trends", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Computed daily trends!")

# Run the function immediately
compute_trends()

