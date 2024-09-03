"""
This module contains all the queries that will be used to interact with the database.
"""
from db_connection import get_connection

def get_tasks_by_user(user_id):
    """
    Function to get all tasks for a specific user by user_id

    Args:
    user_id: id of the user

    Returns:
    list -- List of tasks for the user
    """
    query = 'SELECT * FROM tasks WHERE user_id = %s'
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            return cursor.fetchall()

def get_tasks_by_status(status_name):
    """
    Function to get all tasks by status name

    Args:
    status_name: name of the status

    Returns:
    list -- List of tasks with the status
    """
    query = """
    SELECT t.* FROM tasks t
    JOIN status s ON t.status_id = s.id
    WHERE s.name = %s
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (status_name,))
            return cursor.fetchall()

def update_task_status(task_id, new_status):
    """
    Function to update the status of a task

    Args:
    task_id: id of the task

    Returns:
    None
    """
    query = """
    UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = %s) WHERE id = %s
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_status, task_id))
            conn.commit()

def get_users_with_no_tasks():
    """
    Function to get users with no tasks

    Returns:
    list -- List of users with no tasks
    """
    query = """
    SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def add_task(title, description, status_name, user_id):
    """
    Function to add a new task for a specific user

    Args:
    title: title of the task
    description: description of the task
    status_name: name of the status
    user_id: id of the user

    Returns:
    None
    """
    query = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), %s)
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (title, description, status_name, user_id))
            conn.commit()

def get_incomplete_tasks():
    """
    Function to get all incomplete tasks

    Returns:
    list -- List of incomplete tasks
    """
    query = """
    SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def delete_task(task_id):
    """
    Function to delete a task by task_id

    Args:
    task_id: id of the task

    Returns:
    None
    """
    query = 'DELETE FROM tasks WHERE id = %s'
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (task_id,))
            conn.commit()

def find_users_by_email(email_pattern):
    """
    Function to find users by email pattern

    Args:
    email_pattern: pattern to search for in email

    Returns:
    list -- List of users matching the
    """
    query = 'SELECT * FROM users WHERE email LIKE %s'
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (email_pattern,))
            return cursor.fetchall()

def update_user_name(user_id, new_name):
    """
    Function to update the name of a user

    Args:
    user_id: id of the user
    new_name: new name for the user

    Returns:
    None
    """
    query = 'UPDATE users SET fullname = %s WHERE id = %s'
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_name, user_id))
            conn.commit()

def get_tasks_count_by_status():
    """
    Function to get the count of tasks by status

    Returns:
    list -- List of tasks count by status
    """
    query = """
    SELECT s.name, COUNT(t.id) as task_count
    FROM status s
    LEFT JOIN tasks t ON s.id = t.status_id
    GROUP BY s.name
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
