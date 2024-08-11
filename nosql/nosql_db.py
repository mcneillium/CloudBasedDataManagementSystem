from pymongo import MongoClient

# This class manages interactions with a MongoDB NoSQL database.
class NoSQLDatabaseManager:
    def __init__(self, db_name="cloud_data", collection_name="users"):
        # Initialize the connection to the MongoDB database.
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_user(self, user_data):
        # Insert a new user document into the users collection.
        try:
            self.collection.insert_one(user_data)
            print("User inserted:", user_data)
        except Exception as e:
            print("Error inserting user:", e)

    def fetch_users(self):
        # Fetch all users from the users collection.
        return list(self.collection.find())

    def close(self):
        # Close the connection to the MongoDB database.
        self.client.close()

# Example usage:
if __name__ == "__main__":
    db_manager = NoSQLDatabaseManager()
    db_manager.insert_user({"name": "Alice", "email": "alice@example.com"})
    db_manager.insert_user({"name": "Bob", "email": "bob@example.com"})

    users = db_manager.fetch_users()
    for user in users:
        print(user)

    db_manager.close()
