import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

a.commit()

print("Table created successfully")

a.close()