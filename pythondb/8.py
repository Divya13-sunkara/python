import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT * FROM students WHERE id = 3")

row = c.fetchone()

print(row)

a.close()