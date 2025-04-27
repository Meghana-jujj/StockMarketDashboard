import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('stocks.db')  # Ensure 'stocks.db' is in the correct location

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute the query to get the schema of the 'daily_trends' table
cursor.execute("PRAGMA table_info(daily_trends)")

# Fetch all the columns information
columns = cursor.fetchall()

# Print the column names and types
print("Columns in 'daily_trends' table:")
for column in columns:
    print(column)

# Close the connection
conn.close()
