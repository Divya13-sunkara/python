import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("SELECT MAX(marks), MIN(marks) FROM students")

result = c.fetchone()

print("Highest marks:", result[0])
print("Lowest marks:", result[1])

a.close()