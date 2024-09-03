
# Task Management System

This repository contains a set of scripts for managing a PostgreSQL-based task management system. It includes functionality for creating database tables, seeding these tables with sample data, and performing various queries.

## Prerequisites

- Python 3.8+
- PostgreSQL
- Python libraries: `psycopg2`, `python-dotenv`, `Faker`

## Setup and Usage Instructions

```bash
# Install required Python libraries
pip install psycopg2 python-dotenv Faker

# Create a .env file in the root directory with your database connection details:
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password

# Run the create_tables.py script to set up the database tables
python create_tables.py

# Seed the database with initial data
python seed.py

# Use the main.py script to interact with the database. Example commands:
python main.py tasks_by_user       # Fetches tasks for a specific user by user ID.
python main.py tasks_by_status     # Fetches tasks by their status.
python main.py users_with_no_tasks # Fetches users with no tasks assigned
python main.py incomplete_tasks    # Fetches all incomplete tasks
python main.py tasks_count_by_status # Shows tasks stats per status
```