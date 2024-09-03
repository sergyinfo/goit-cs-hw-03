
# MongoDB Cat Management System

This project demonstrates a simple MongoDB management system for cat records using Python and PyMongo. It includes CRUD operations to create, read, update, and delete cat data in a MongoDB database.

## Prerequisites

- Python 3.8 or higher
- MongoDB instance (local or MongoDB Atlas)
- PyMongo library
- python-dotenv library for managing environment variables

## Setup

1. **Install Required Libraries**:

   Use pip to install the necessary Python packages:

   ```bash
   pip install pymongo python-dotenv
   ```

2. **Environment Configuration**:

   Create a `.env` file in your project directory with the MongoDB connection details:

   ```plaintext
   MONGO_URI=mongodb://localhost:27017/  # Or your MongoDB connection string
   DB_NAME=cats_db                       # Database name
   ```

## Running the Script

You can perform various operations by passing arguments to `main.py`. Here are the available commands:

- **Create a Cat Record**:
  ```bash
  python main.py --create "Cat Name" Age "Feature1, Feature2"
  ```
- **Get All Cat Records**:
  ```bash
  python main.py --get-all
  ```
- **Get a Cat by Name**:
  ```bash
  python main.py --get-by-name "Cat Name"
  ```
- **Update Cat's Age**:
  ```bash
  python main.py --update-age "Cat Name" NewAge
  ```
- **Add Feature to Cat**:
  ```bash
  python main.py --add-feature "Cat Name" "New Feature"
  ```
- **Delete a Cat by Name**:
  ```bash
  python main.py --delete "Cat Name"
  ```
- **Delete All Cats**:
  ```bash
  python main.py --delete-all
  ```