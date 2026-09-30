import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT * FROM students WHERE marks BETWEEN 60 AND 90")

rows = c.fetchall()

for row in rows:
    print(row)

a.close()