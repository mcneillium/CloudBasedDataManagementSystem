import mongomock

from nosql.nosql_db import NoSQLDatabaseManager
from sql.sql_db import SQLDatabaseManager


def test_sql_insert_fetch_and_duplicate_email():
    db = SQLDatabaseManager(":memory:")
    db.create_table()
    assert db.insert_user("Alice", "alice@example.com") is True
    assert db.insert_user("Alice again", "alice@example.com") is False
    assert db.fetch_users() == [(1, "Alice", "alice@example.com")]
    db.close()


def test_nosql_insert_fetch_and_clear():
    db = NoSQLDatabaseManager(client=mongomock.MongoClient())
    db.insert_user({"name": "Bob", "email": "bob@example.com"})
    users = db.fetch_users()
    assert [(u["name"], u["email"]) for u in users] == [("Bob", "bob@example.com")]
    db.clear_users()
    assert db.fetch_users() == []
    db.close()


def test_nosql_requires_a_connection_string(monkeypatch):
    monkeypatch.delenv("MONGO_URI", raising=False)
    import nosql.nosql_db as mod
    monkeypatch.setattr(mod.os, "getenv", lambda k, d=None: None)
    try:
        NoSQLDatabaseManager()
    except ValueError as e:
        assert "MONGO_URI" in str(e)
    else:
        raise AssertionError("expected ValueError without MONGO_URI")


def test_nosql_refuses_a_duplicate_email_like_sql():
    # The unique index gives the collection the same rule as the SQL table.
    db = NoSQLDatabaseManager(client=mongomock.MongoClient())
    assert db.insert_user({"name": "Bob", "email": "bob@example.com"}) is True
    assert db.insert_user({"name": "Bob again", "email": "bob@example.com"}) is False
    assert len(db.fetch_users()) == 1
