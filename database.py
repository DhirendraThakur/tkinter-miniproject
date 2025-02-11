import sqlite3
conn = sqlite3.connect("cities.db")
cursor = conn.cursor()





# Create a users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        address TEXT,
        email TEXT,
        password TEXT
    )
""")
conn.commit()

# Function to insert a user into the database
def insert_user(username, address, email, password):
    cursor.execute("INSERT INTO users (username, address, email, password) VALUES (?, ?, ?, ?)",
                   (username, address, email, password))
    conn.commit()

# Function to close the database
def close_db():
    conn.close()