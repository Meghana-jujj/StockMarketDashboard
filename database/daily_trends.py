import sqlite3
import random
from datetime import datetime, timedelta

# Connect to database
conn = sqlite3.connect('C:/Users/megha/OneDrive/StockMarketDashboard/database/stocks.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    avg_price REAL NOT NULL
)
''')

# Insert sample data
start_date = datetime(2024, 1, 1)

data = []
for i in range(100):  # 100 days
    date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
    avg_price = round(150 + random.uniform(-5, 5), 2)
    data.append(('AAPL', date, avg_price))

cursor.executemany("INSERT INTO daily_trends (symbol, date, avg_price) VALUES (?, ?, ?)", data)
conn.commit()
conn.close()

print("✅ Sample data inserted successfully!")
