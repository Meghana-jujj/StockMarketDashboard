import sqlite3

# Connect to the SQLite database (this will create it if it doesn't exist)
conn = sqlite3.connect('stocks.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the 'daily_trends' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_trends (
    symbol TEXT,
    date DATE,
    avg_price REAL,
    price_std REAL
);
''')

# Insert some sample data into the 'daily_trends' table
cursor.executemany('''
INSERT INTO daily_trends (symbol, date, avg_price, price_std) VALUES (?, ?, ?, ?)
''', [
    ('AAPL', '2025-04-01', 145.67, 1.23),
    ('GOOGL', '2025-04-01', 2520.75, 2.34),
    ('AMZN', '2025-04-01', 3350.90, 3.45),
    ('AAPL', '2025-04-02', 146.23, 1.12),
    ('GOOGL', '2025-04-02', 2530.85, 2.56),
    ('MSFT', '2025-04-01', 300.50, 0.99),
    ('TSLA', '2025-04-01', 675.30, 1.10)
])

# Commit the changes to the database
conn.commit()

# Output a success message
print("Sample data inserted into 'daily_trends' table.")

# Close the connection to the database
conn.close()
