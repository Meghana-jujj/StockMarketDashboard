import sqlite3

# Connect to SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect('C:/Users/megha/OneDrive/StockMarketDashboard/database/stocks.db')
cursor = conn.cursor()

# Create a table called 'daily_trends' to store stock data
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    avg_price REAL NOT NULL
);
''')

# Sample stock data (symbol, date, average price)
sample_data = [
    ('AAPL', '2021-01-01', 130.0),
    ('AAPL', '2021-01-02', 132.5),
    ('AAPL', '2021-01-03', 131.0),
    ('AAPL', '2021-01-04', 133.2),
    ('TSLA', '2021-01-01', 700.0),
    ('TSLA', '2021-01-02', 710.5),
    ('TSLA', '2021-01-03', 715.0),
    ('AMZN', '2021-01-01', 3300.0),
    ('AMZN', '2021-01-02', 3325.0)
]

# Insert sample data into the 'daily_trends' table
cursor.executemany('''
INSERT INTO daily_trends (symbol, date, avg_price)
VALUES (?, ?, ?)
''', sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and sample data inserted successfully!")
