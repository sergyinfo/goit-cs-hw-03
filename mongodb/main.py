"""
A simple command line interface for interacting with the database.

Usage: python main.py [command]

Commands:
    - get_all_cats
    - get_cat_by_name
    - update_cat_age
    - add_feature_to_cat
    - delete_cat_by_name
    - delete_all_cats
"""
import os
import argparse
from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_database():
    """ 
    Connect to MongoDB and return a database instance. 

    Returns:
    A database instance.
    """
    try:
        # Retrieve connection details from environment variables
        client = MongoClient(os.getenv('MONGO_URI'))
        return client[os.getenv('DB_NAME')]
    except errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)

def create_cat(db, name, age, features):
    """ 
    Create a new cat document. 

    Args:
    db: database instance
    name: cat's name
    age: cat's age
    features: list of cat's features

    Returns:
    The id of the newly created cat document.
    """
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return db.cats.insert_one(cat).inserted_id

def get_all_cats(db):
    """ 
    Retrieve all cats from the collection. 

    Args:
    db: database instance

    Returns:
    A list of cat documents.
    """
    cats = list(db.cats.find())
    for cat in cats:
        print(cat)

def get_cat_by_name(db, name):
    """ 
    Retrieve a cat by name. 

    Args:
    db: database instance
    name: cat's name

    Returns:
    A cat document
    """
    cat = db.cats.find_one({"name": name})
    print(cat)

def update_cat_age(db, name, new_age):
    """ 
    Update the age of a cat by name. 

    Args:
    db: database instance
    name: cat's name
    new_age: new age of the cat

    Returns:
    The result of the update operation
    """
    result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Updated:", result.modified_count > 0)

def add_feature_to_cat(db, name, feature):
    """ 
    Add a new feature to the cat's features list. 

    Args:
    db: database instance
    name: cat's name
    feature: new feature to add

    Returns:
    The result of the update operation
    """
    result = db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
    print("Feature added:", result.modified_count > 0)

def delete_cat_by_name(db, name):
    """ 
    Delete a cat by name. 

    Args:
    db: database instance

    Returns:
    The result of the delete operation
    """
    result = db.cats.delete_one({"name": name})
    print("Deleted:", result.deleted_count > 0)

def delete_all_cats(db):
    """ 
    Delete all cats from the collection. 

    Args:
    db: database instance

    Returns:
    The result of the delete operation
    """
    result = db.cats.delete_many({})
    print("Deleted all cats:", result.deleted_count > 0)


def setup_arg_parser():
    """ Setup and return the argument parser. """
    parser = argparse.ArgumentParser(description="MongoDB Cat Management System")
    parser.add_argument("--create", help="Create a new cat record", nargs=3, metavar=("NAME", "AGE", "FEATURES"))
    parser.add_argument("--get-all", help="Retrieve all cat records", action="store_true")
    parser.add_argument("--get-by-name", help="Retrieve a cat by name", metavar="NAME")
    parser.add_argument("--update-age", help="Update the age of a cat", nargs=2, metavar=("NAME", "AGE"))
    parser.add_argument("--add-feature", help="Add a feature to a cat", nargs=2, metavar=("NAME", "FEATURE"))
    parser.add_argument("--delete", help="Delete a cat by name", metavar="NAME")
    parser.add_argument("--delete-all", help="Delete all cat records", action="store_true")
    return parser

def main():
    """
    Main function to demonstrate the usage of the functions.

    Usage:
    python main.py --create "Whiskers" 5 "Cute, Playful"
    python main.py --get-all
    python main.py --get-by-name "Whiskers"
    python main.py --update-age "Whiskers" 6
    python main.py --add-feature "Whiskers" "Fluffy"
    python main.py --delete "Whiskers"
    python main.py --delete-all
    """
    db = get_database()
    if db is None:
        print("Failed to connect to MongoDB.")
        return

    parser = setup_arg_parser()
    args = parser.parse_args()

    if args.create:
        name, age, features = args.create[0], int(args.create[1]), args.create[2].split(',')
        create_cat(db, name, age, features)

    if args.get_all:
        get_all_cats(db)

    if args.get_by_name:
        get_cat_by_name(db, args.get_by_name)

    if args.update_age:
        name, new_age = args.update_age[0], int(args.update_age[1])
        update_cat_age(db, name, new_age)

    if args.add_feature:
        name, feature = args.add_feature[0], args.add_feature[1]
        add_feature_to_cat(db, name, feature)

    if args.delete:
        delete_cat_by_name(db, args.delete)

    if args.delete_all:
        delete_all_cats(db)

if __name__ == '__main__':
    main()
