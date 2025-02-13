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
    


# Create a  table for cities if it doesn't exist (Cities Table Database is here)




# Function to create a connection to the database
def create_connection():
    con = sqlite3.connect('cities.db')  # Connect to the database
    cur = con.cursor()  # Create a cursor object to execute SQL queries

    #Create the cities table if it doesn't already exist
    cur.execute('''CREATE TABLE IF NOT EXISTS cities_table (
                        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT NOT NULL)''')
    con.commit()
    return con, cur

