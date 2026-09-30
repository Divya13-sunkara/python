import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT course, COUNT(*) FROM students GROUP BY course")

rows = c.fetchall()

for row in rows:
    print("Course:", row[0], "Students:", row[1])

a.close()