"""
This script is used to seed the database with dummy data. 
It uses the Faker library to generate random data for users and tasks.
"""
import random
from db_connection import get_connection
from faker import Faker


fake = Faker()

def insert_users(cursor, count=10):
    """
    Function to insert users into the database

    Args:
    cursor: cursor object to execute queries
    count: number of users to insert

    Returns:
    None
    """
    for _ in range(count):
        fullname = fake.name()
        email = fake.unique.email()
        cursor.execute('INSERT INTO users (fullname, email) VALUES (%s, %s)', (fullname, email))


def insert_tasks(cursor, count=100):
    """
    Function to insert tasks into the database

    Args:
    cursor: cursor object to execute queries
    count: number of tasks to insert

    Returns:
    None
    """
    # Fetch user IDs
    cursor.execute('SELECT id FROM users')
    user_ids = [row['id'] for row in cursor.fetchall()]  # Adjusted to use column name

    # Fetch status IDs
    cursor.execute('SELECT id FROM status')
    status_ids = [row['id'] for row in cursor.fetchall()]  # Adjusted to use column name

    for _ in range(count):
        title = fake.sentence()
        description = fake.text()
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute(
            'INSERT INTO tasks (title, description, status_id, user_id) '
            'VALUES (%s, %s, %s, %s)',
            (title, description, status_id, user_id)
        )


def main():
    """
    Function to seed the database with dummy data

    Returns:
    None
    """
    conn = get_connection()  # Utilizes the secure connection setup
    with conn.cursor() as cursor:
        insert_users(cursor)
        insert_tasks(cursor)
        conn.commit()
    conn.close()
    print("Data seeded successfully.")

if __name__ == '__main__':
    main()
