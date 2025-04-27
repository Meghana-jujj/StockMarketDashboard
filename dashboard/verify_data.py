import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('stocks.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Fetch all rows from the 'daily_trends' table
cursor.execute('SELECT * FROM daily_trends')

# Fetch all results
rows = cursor.fetchall()

# Print out the rows
print("Data in 'daily_trends' table:")
for row in rows:
    print(row)

# Close the connection
conn.close()
