import sqlite3

conn = sqlite3.connect("C:/Users/megha/OneDrive/StockMarketDashboard/database/stocks.db")
cur = conn.cursor()

# Check the data in daily_trends table
cur.execute("SELECT * FROM daily_trends LIMIT 10")
print(cur.fetchall())

conn.close()
