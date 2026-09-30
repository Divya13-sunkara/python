import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT course, AVG(marks) FROM students GROUP BY course")

rows = c.fetchall()

for row in rows:
    print("Course:", row[0], "Average marks:", row[1])

a.close()