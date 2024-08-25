import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

class NoSQLDatabaseManager:
    def __init__(self, db_name="DatabaseProject"):
        # Get the connection string from the environment variable
        mongo_uri = os.getenv('MONGO_URI')
        if not mongo_uri:
            raise ValueError("No MongoDB URI found. Please set the MONGO_URI environment variable.")
        
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db["users"]  # Use the "users" collection in your database

    def insert_user(self, user_data):
        """Insert a new user document into the NoSQL database."""
        self.collection.insert_one(user_data)

    def fetch_users(self):
        """Fetch all user documents from the NoSQL database."""
        return list(self.collection.find())

    def clear_users(self):
        """Clear all user documents from the NoSQL database."""
        self.collection.delete_many({})

    def close(self):
        """Close the connection to the NoSQL database."""
        self.client.close()

# Example usage:
if __name__ == "__main__":
    nosql_manager = NoSQLDatabaseManager()
    
    # Insert a new user
    nosql_manager.insert_user({"name": "Alice", "email": "alice@example.com"})
    
    # Fetch and print all users
    users = nosql_manager.fetch_users()
    for user in users:
        print(user)
    
    # Clear all users
    nosql_manager.clear_users()
    
    # Close the connection
    nosql_manager.close()
