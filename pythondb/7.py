import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT * FROM students WHERE course = 'Python'")

rows = c.fetchall()

for row in rows:
    print(row)

a.close()