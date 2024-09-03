"""
A simple command line interface for interacting with the database.

Usage: python main.py [command]

Commands:
    - create_tables
    - seed_data
    - tasks_by_user
    - tasks_by_status
    - users_with_no_tasks
    - incomplete_tasks
    - tasks_count_by_status
"""
import sys
from create_tables import create_tables
from seed import main as seed_data
from queries import (
    get_tasks_by_user, 
    get_tasks_by_status, 
    get_users_with_no_tasks, 
    get_incomplete_tasks, 
    get_tasks_count_by_status
)

def print_tasks(tasks):
    """
    Function to print tasks

    Args:
    tasks: list of tasks

    Returns:
    None
    """
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"Task ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")

def main():
    """
    Main function to run the command line interface

    Returns:
    None
    """
    commands = {
        'create_tables': create_tables,
        'seed_data': seed_data,
        'tasks_by_user': lambda: print_tasks(get_tasks_by_user(input("Enter user ID: "))),
        'tasks_by_status': lambda: print_tasks(get_tasks_by_status(input("Enter status name: "))),
        'users_with_no_tasks': lambda: print(get_users_with_no_tasks()),
        'incomplete_tasks': lambda: print_tasks(get_incomplete_tasks()),
        'tasks_count_by_status': lambda: print(get_tasks_count_by_status())
    }

    if len(sys.argv) < 2:
        print("Usage: python main.py [command]")
        print("Commands:")
        for command in commands:
            print(f"  - {command}")
        return

    command = sys.argv[1]
    if command in commands:
        commands[command]()
    else:
        print(f"Invalid command. Available commands are: {list(commands.keys())}")

if __name__ == "__main__":
    main()
