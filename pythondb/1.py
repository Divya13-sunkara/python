import sqlite3

a = sqlite3.connect("college.db")

print("Database created successfully")

a.close()