import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT name FROM students")

rows = c.fetchall()

for row in rows:
    print(row[0])

a.close()