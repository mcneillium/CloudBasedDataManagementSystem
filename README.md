# Cloud-Based Data Management System

[![tests](https://github.com/mcneillium/CloudBasedDataManagementSystem/actions/workflows/tests.yml/badge.svg)](https://github.com/mcneillium/CloudBasedDataManagementSystem/actions/workflows/tests.yml)

The same small "users" dataset managed two ways: in a relational database
(SQLite) and in a document database (MongoDB, local or Atlas), with a Tkinter
GUI to insert and list records in each.

Case study: [paulmartinmcneill.com/projects/cloud-data-management](https://paulmartinmcneill.com/projects/cloud-data-management/)

## What it shows

- **SQL (`sql/sql_db.py`):** a `users` table with a unique email constraint;
  inserting a duplicate email is refused and reported.
- **NoSQL (`nosql/nosql_db.py`):** a `users` collection in MongoDB; insert,
  list and clear documents.
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

## Licence

MIT, see [LICENSE](LICENSE).
