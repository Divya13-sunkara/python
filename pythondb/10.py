import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

c.execute("DELETE FROM students WHERE id = 4")

a.commit()

c.execute("SELECT * FROM students")

for row in c.fetchall():
    print(row)

a.close()