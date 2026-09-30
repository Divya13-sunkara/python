import sqlite3

a = sqlite3.connect("college.db")
c = a.cursor()

data = [
    (1, "Divya", 18, "Python", 85),
    (2, "Sai", 19, "Java", 72),
    (3, "divi", 18, "Python", 90),
    (4, "lokesh", 20, "SQL", 68),
    (5, "teja", 19, "Python", 78)
]

c.executemany("INSERT OR IGNORE INTO students VALUES(?,?,?,?,?)", data)

a.commit()

print("5 records inserted successfully")

a.close()