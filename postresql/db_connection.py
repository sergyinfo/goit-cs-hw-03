"""
Database connection module
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from the .env file

def get_connection():
    """
    Function to get a connection to the database

    Returns:
    psycopg2.extensions.connection -- A connection to the PostgreSQL database
    """
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        cursor_factory=RealDictCursor  # Using RealDictCursor to get column names with data
    )
