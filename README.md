
# Cloud-Based Data Management System

## Overview

This project demonstrates a cloud-based database management system implemented using both SQL and NoSQL databases. The SQL component is handled by SQLite, while the NoSQL component is managed using MongoDB. This system is designed to showcase how to interact with different types of databases, insert and retrieve data, and manage database connections in a cloud environment.

## Project Structure

- **`sql/`**: Contains the SQL database management system implementation using SQLite.
- **`nosql/`**: Contains the NoSQL database management system implementation using MongoDB.

## Features

- **SQL Database Management**:
  - Implemented with SQLite.
  - Supports creating tables, inserting records, and fetching data.
  
- **NoSQL Database Management**:
  - Implemented with MongoDB.
  - Supports inserting documents and retrieving data.

## How to Run

### SQL Database

1. Navigate to the `sql/` directory.
   ```bash
   cd sql
   ```

2. Run the `sql_db.py` script.
   ```bash
   python sql_db.py
   ```

### NoSQL Database

1. Ensure that MongoDB is running on your local machine or use MongoDB Atlas for a cloud-hosted solution.

2. Navigate to the `nosql/` directory.
   ```bash
   cd nosql
   ```

3. Run the `nosql_db.py` script.
   ```bash
   python nosql_db.py
   ```

### Contributions

Contributions are welcome! Feel free to submit pull requests with additional features or improvements.

### License
This project is licensed under the MIT License.
