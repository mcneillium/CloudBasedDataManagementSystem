import tkinter as tk
from tkinter import messagebox, scrolledtext
from sql.sql_db import SQLDatabaseManager 
from nosql.nosql_db import NoSQLDatabaseManager  

# Initialize the database managers
sql_manager = SQLDatabaseManager()
nosql_manager = NoSQLDatabaseManager()

# Create the main window
root = tk.Tk()
root.title("Paul Martin McNeill's Database Management System")
root.geometry("650x600")

# Function to switch between SQL and NoSQL panels
def switch_panel(panel):
    sql_frame.pack_forget()
    nosql_frame.pack_forget()
    if panel == "SQL":
        sql_frame.pack(fill="both", expand=True)
    elif panel == "NoSQL":
        nosql_frame.pack(fill="both", expand=True)

# SQL Functions
def create_sql_table():
    sql_manager.create_table()
    messagebox.showinfo("Info", "SQL Users table created successfully.")

def add_sql_user():
    name = sql_name_entry.get()
    email = sql_email_entry.get()
    if name and email:
        sql_manager.insert_user(name, email)
        messagebox.showinfo("Info", "User added to SQL database successfully.")
        sql_name_entry.delete(0, tk.END)
        sql_email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and email.")

def view_sql_users():
    users = sql_manager.fetch_users()
    sql_display_area.delete(1.0, tk.END)
    if users:
        for user in users:
            sql_display_area.insert(tk.END, f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}\n")
    else:
        sql_display_area.insert(tk.END, "No users found in SQL database.")

def clear_sql_table():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all SQL user records?"):
        sql_manager.cursor.execute("DELETE FROM users")
        sql_manager.connection.commit()
        messagebox.showinfo("Info", "All SQL user records have been cleared.")
        sql_display_area.delete(1.0, tk.END)

# NoSQL Functions
def add_nosql_document():
    name = nosql_name_entry.get()
    email = nosql_email_entry.get()
    if name and email:
        user_data = {"": name, "": email}
        nosql_manager.insert_user(user_data)
        messagebox.showinfo("Info", "User added to NoSQL database successfully.")
        nosql_name_entry.delete(0, tk.END)
        nosql_email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and email.")

def view_nosql_collection():
    users = nosql_manager.fetch_users()
    nosql_display_area.delete(1.0, tk.END)
    if users:
        for user in users:
            nosql_display_area.insert(tk.END, f"Name: {user.get('name')}, Email: {user.get('email')}\n")
    else:
        nosql_display_area.insert(tk.END, "No users found in NoSQL database.")

def clear_nosql_collection():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all NoSQL user records?"):
        nosql_manager.collection.delete_many({})
        messagebox.showinfo("Info", "All NoSQL user records have been cleared.")
        nosql_display_area.delete(1.0, tk.END)

# Top menu for switching between SQL and NoSQL
menu_frame = tk.Frame(root)
menu_frame.pack(side="top", fill="x")

sql_button = tk.Button(menu_frame, text="SQL Database", command=lambda: switch_panel("SQL"), width=20)
sql_button.pack(side="left", padx=5, pady=5)

nosql_button = tk.Button(menu_frame, text="NoSQL Database", command=lambda: switch_panel("NoSQL"), width=20)
nosql_button.pack(side="left", padx=5, pady=5)

# SQL Panel
sql_frame = tk.Frame(root)
tk.Label(sql_frame, text="SQL Database Operations", font=("Helvetica", 14)).pack(pady=10)

# Explanatory text for the SQL section
sql_instructions = tk.Label(sql_frame, text="Manage your SQL database here. You can create a table, add users, view all users, and clear the table.", justify="left")
sql_instructions.pack(pady=5)

sql_name_entry = tk.Entry(sql_frame, width=40)
sql_name_entry.pack(pady=5)
sql_name_entry.insert(0, "")
sql_name_entry_label = tk.Label(sql_frame, text="Enter the name of the user you want to add.", font=("Helvetica", 10, "italic"))
sql_name_entry_label.pack()

sql_email_entry = tk.Entry(sql_frame, width=40)
sql_email_entry.pack(pady=5)
sql_email_entry.insert(0, "")
sql_email_entry_label = tk.Label(sql_frame, text="Enter the email of the user you want to add.", font=("Helvetica", 10, "italic"))
sql_email_entry_label.pack()

tk.Button(sql_frame, text="Create Table", command=create_sql_table, width=20).pack(pady=5)
create_table_label = tk.Label(sql_frame, text="Click to create the users table if it doesn't exist.", font=("Helvetica", 10, "italic"))
create_table_label.pack()

tk.Button(sql_frame, text="Add User", command=add_sql_user, width=20).pack(pady=5)
add_user_label = tk.Label(sql_frame, text="Click to add the user to the SQL database.", font=("Helvetica", 10, "italic"))
add_user_label.pack()

tk.Button(sql_frame, text="View Users", command=view_sql_users, width=20).pack(pady=5)
view_users_label = tk.Label(sql_frame, text="Click to view all users stored in the SQL database.", font=("Helvetica", 10, "italic"))
view_users_label.pack()

tk.Button(sql_frame, text="Clear Table", command=clear_sql_table, width=20, bg="red").pack(pady=5)
clear_table_label = tk.Label(sql_frame, text="Click to clear all users from the SQL database.", font=("Helvetica", 10, "italic"))
clear_table_label.pack()

sql_display_area = scrolledtext.ScrolledText(sql_frame, width=50, height=10)
sql_display_area.pack(pady=10)

# NoSQL Panel
nosql_frame = tk.Frame(root)
tk.Label(nosql_frame, text="NoSQL Database Operations", font=("Helvetica", 14)).pack(pady=10)

# Explanatory text for the NoSQL section
nosql_instructions = tk.Label(nosql_frame, text="Manage your NoSQL database here. You can add documents, view the collection, and clear the collection.", justify="left")
nosql_instructions.pack(pady=5)

nosql_name_entry = tk.Entry(nosql_frame, width=40)
nosql_name_entry.pack(pady=5)
nosql_name_entry.insert(0, "Enter Name")
nosql_name_entry_label = tk.Label(nosql_frame, text="Enter the name to be included in the document.", font=("Helvetica", 10, "italic"))
nosql_name_entry_label.pack()

nosql_email_entry = tk.Entry(nosql_frame, width=40)
nosql_email_entry.pack(pady=5)
nosql_email_entry.insert(0, "Enter Email")
nosql_email_entry_label = tk.Label(nosql_frame, text="Enter the email to be included in the document.", font=("Helvetica", 10, "italic"))
nosql_email_entry_label.pack()

tk.Button(nosql_frame, text="Add Document", command=add_nosql_document, width=20).pack(pady=5)
add_document_label = tk.Label(nosql_frame, text="Click to add the document to the NoSQL database.", font=("Helvetica", 10, "italic"))
add_document_label.pack()

tk.Button(nosql_frame, text="View Collection", command=view_nosql_collection, width=20).pack(pady=5)
view_collection_label = tk.Label(nosql_frame, text="Click to view all documents in the NoSQL collection.", font=("Helvetica", 10, "italic"))
view_collection_label.pack()

tk.Button(nosql_frame, text="Clear Collection", command=clear_nosql_collection, width=20, bg="red").pack(pady=5)
clear_collection_label = tk.Label(nosql_frame, text="Click to clear all documents from the NoSQL database.", font=("Helvetica", 10, "italic"))
clear_collection_label.pack()

nosql_display_area = scrolledtext.ScrolledText(nosql_frame, width=50, height=10)
nosql_display_area.pack(pady=10)

# Start with SQL panel visible
switch_panel("SQL")

# Footer with your name
footer_label = tk.Label(root, text="Created by Paul Martin McNeill", font=("Helvetica", 10, "italic"))
footer_label.pack(side="bottom", pady=10)

# Run the main loop
root.mainloop()
