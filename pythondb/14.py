import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT COUNT(*) FROM students")

result = c.fetchone()

print("Total students:", result)

a.close()