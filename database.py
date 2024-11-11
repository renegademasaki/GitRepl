import sqlite3

def alter_table():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor
    c = conn.cursor()

    # Alter the table
    c.execute("ALTER TABLE users ADD COLUMN occupation TEXT")

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
    
def delete_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS users')
    conn.commit()
    conn.close()

def delete_user():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object
    c = conn.cursor()

    # Delete the user from the database
    c.execute("DELETE FROM users WHERE id > 5")

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def create_user():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)", ('Alice', 30, 'female'))
    c.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)", ('Bob', 25, 'male'))
    c.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)", ('Charlie', 35, 'male'))

    conn.commit()
    conn.close()

def create_occupation():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_occupations (name, occupation) VALUES (?, ?)", ('Alice', 'Software Engineer'))
    c.execute("INSERT INTO user_occupations (name, occupation) VALUES (?, ?)", ('Bob', 'Data Scientist'))
    c.execute("INSERT INTO user_occupations (name, occupation) VALUES (?, ?)", ('Charlie', 'Marketing Manager'))

    conn.commit()
    conn.close()

def print_database():
    conn = sqlite3.connect('mydatabase.db')

    c = conn.cursor()

    c.execute("SELECT * FROM users")

    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

def create_database():
    # Create a connection to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table (if it doesn't exist)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT
                )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_occupations (
    id INTEGER PRIMARY KEY,
    name TEXT,
    occupation TEXT
                )''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    print("SQLite database created successfully!")
