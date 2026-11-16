import sqlite3


class SQLDatabaseManager:
    """Users in an SQLite table. The table's schema enforces one account per email."""

    def __init__(self, db_name: str = "cloud_data.db") -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self) -> None:
        """Create the users table if it is not there yet."""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT UNIQUE NOT NULL)""")
        self.connection.commit()

    def insert_user(self, name: str, email: str) -> bool:
        """Insert a user. Returns True if inserted, False if the email is already taken."""
        try:
            self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            # The UNIQUE constraint on email refused a duplicate.
            return False

    def fetch_users(self) -> list[tuple[int, str, str]]:
        """Every user as (id, name, email)."""
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close(self) -> None:
        self.connection.close()


if __name__ == "__main__":
    db_manager = SQLDatabaseManager()
    db_manager.create_table()
    db_manager.insert_user("Alice", "alice@example.com")
    db_manager.insert_user("Bob", "bob@example.com")

    for user in db_manager.fetch_users():
        print(user)

    db_manager.close()
