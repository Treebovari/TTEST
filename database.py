# database.py

"""
Database initialization and management functions.
"""

import sqlite3


def init_db(db_name=':memory:'):
    """
    Initialize the database.
    Creates a connection to the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    """
    Create a sample table in the database.
    """
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sample (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )' )
    conn.commit()


def insert_data(conn, name, age):
    """
    Insert data into the sample table.
    """
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO sample (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()


def fetch_data(conn):
    """
    Fetch all data from the sample table.
    """
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM sample''')
    return cursor.fetchall()


# Example usage:
if __name__ == '__main__':
    connection = init_db('test.db')  # Change 'test.db' to your desired database name
    create_table(connection)
    insert_data(connection, 'Alice', 30)
    print(fetch_data(connection))
    connection.close()