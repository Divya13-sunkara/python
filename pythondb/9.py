import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("UPDATE students SET marks = 95 WHERE id = 1")

con.commit()

cur.execute("SELECT * FROM students WHERE id = 1")

print(cur.fetchone())

con.close()