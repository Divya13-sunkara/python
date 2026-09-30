import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT AVG(marks) FROM students")

result = c.fetchone()

print("Average marks:", result[0])

a.close()