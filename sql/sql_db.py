import sqlite3

# This class manages interactions with an SQLite database.
class SQLDatabaseManager:
    def __init__(self, db_name="cloud_data.db"):
        # Initialize the connection to the SQLite database.
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        # Create a sample table to store user data.
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT UNIQUE NOT NULL)''')
        self.connection.commit()

    def insert_user(self, name, email):
        # Insert a new user into the users table.
        # Returns True if inserted, False if the email is already taken.
        try:
            self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            # The UNIQUE constraint on email refused a duplicate.
            return False

    def fetch_users(self):
        # Fetch all users from the users table.
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close(self):
        # Close the connection to the database.
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    db_manager = SQLDatabaseManager()
    db_manager.create_table()
    db_manager.insert_user("Alice", "alice@example.com")
    db_manager.insert_user("Bob", "bob@example.com")
    
    users = db_manager.fetch_users()
    for user in users:
        print(user)

    db_manager.close()
