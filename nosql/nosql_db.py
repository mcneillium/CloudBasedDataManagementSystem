import os
from collections.abc import Mapping
from typing import Any

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# Load environment variables from the root .env file
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


class NoSQLDatabaseManager:
    def __init__(
        self, db_name: str = "DatabaseProject", client: MongoClient[dict[str, Any]] | None = None
    ) -> None:
        # A client can be passed in (tests use mongomock); otherwise connect
        # using the MONGO_URI environment variable, read from .env if present.
        if client is None:
            mongo_uri = os.getenv("MONGO_URI")
            if not mongo_uri:
                raise ValueError(
                    "No MongoDB URI found. Please set the MONGO_URI environment variable."
                )
            client = MongoClient(mongo_uri)

        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db["users"]  # Use the "users" collection in your database
        # MongoDB has no table schema, so uniqueness comes from an index. This
        # gives the collection the same rule as the SQL table's UNIQUE email.
        self.collection.create_index("email", unique=True)

    def insert_user(self, user_data: Mapping[str, Any]) -> bool:
        """Insert a new user document.

        Returns True if inserted, False if the email is already taken.
        """
        try:
            self.collection.insert_one(dict(user_data))
            return True
        except DuplicateKeyError:
            return False

    def fetch_users(self) -> list[dict[str, Any]]:
        """Fetch all user documents from the NoSQL database."""
        return list(self.collection.find())

    def clear_users(self) -> None:
        """Clear all user documents from the NoSQL database."""
        self.collection.delete_many({})

    def close(self) -> None:
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
