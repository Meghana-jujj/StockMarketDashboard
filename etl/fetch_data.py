import sqlite3
import time
from datetime import datetime
import random

# Connect to the database (creates if not exists)
conn = sqlite3.connect("../database/stocks.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        timestamp TEXT,
        price REAL,
        volume INTEGER
    )
""")
conn.commit()

# Function to generate mock stock data
def fetch_stock_data(symbol="AAPL"):
    return {
        "symbol": symbol,
        "timestamp": datetime.now().isoformat(),
        "price": round(random.uniform(190, 210), 2),
        "volume": random.randint(1000, 5000)
    }

# Continuously insert stock data every minute
while True:
    data = fetch_stock_data()
    cur.execute(
        "INSERT INTO stock_prices (symbol, timestamp, price, volume) VALUES (?, ?, ?, ?)",
        (data["symbol"], data["timestamp"], data["price"], data["volume"])
    )
    conn.commit()
    print(f"Stored: {data}")
    time.sleep(60)  # Wait for 1 minute
