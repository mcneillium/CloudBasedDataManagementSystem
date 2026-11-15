# Cloud-Based Data Management System

[![tests](https://github.com/mcneillium/CloudBasedDataManagementSystem/actions/workflows/tests.yml/badge.svg)](https://github.com/mcneillium/CloudBasedDataManagementSystem/actions/workflows/tests.yml)

The same small "users" dataset managed two ways: in a relational database
(SQLite) and in a document database (MongoDB, local or Atlas), with a Tkinter
GUI to insert and list records in each.

Case study: [paulmartinmcneill.com/projects/cloud-data-management](https://paulmartinmcneill.com/projects/cloud-data-management/)

![The SQL and NoSQL panels, each listing users added through the GUI](docs/screenshot.png)

## What it shows

- **SQL (`sql/sql_db.py`):** a `users` table with a unique email constraint;
  inserting a duplicate email is refused and reported.
- **NoSQL (`nosql/nosql_db.py`):** a `users` collection in MongoDB; insert,
  list and clear documents. MongoDB has no table schema, so the same
  one-account-per-email rule comes from a unique index on `email`.
- **Both refuse duplicates the same way:** the GUI reports a refused email
  instead of claiming success.
- **Configuration:** the MongoDB connection string is read from the
  `MONGO_URI` environment variable (or a local `.env` file), never from code.
- **Tests:** the SQL manager is tested against an in-memory SQLite database
  and the NoSQL manager against `mongomock`, so the tests need no database
  server. They run on every push.

## Run it

Python 3.10 or later.

```bash
git clone https://github.com/mcneillium/CloudBasedDataManagementSystem.git
cd CloudBasedDataManagementSystem
pip install -r requirements.txt
cp .env.example .env       # then put your own MongoDB connection string in .env
python main_gui.py         # opens the GUI (needs Tkinter)
```

Run the tests:

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

## Changes (November 2026)

- Adding a user whose email was already taken used to show "added
  successfully" while the database had refused it. The GUI now reports it.
- The MongoDB collection now refuses duplicate emails too (unique index), so
  the two stores follow the same rule. A test covers it.
- Adding a SQL user no longer fails if "Create Table" hasn't been clicked first.

## Licence

MIT, see [LICENSE](LICENSE).
