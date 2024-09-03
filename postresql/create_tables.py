"""
Create tables in the database.
"""
from db_connection import get_connection

def create_tables():
    """
    Function to create tables in the database

    Returns:
    None    
    """
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed')
    ON CONFLICT (name) DO NOTHING;
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL REFERENCES status(id),
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
    );
    """
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == '__main__':
    create_tables()
