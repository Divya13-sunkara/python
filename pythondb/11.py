import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

data = [
    (1, "sai", 19, "CSE", 85),
    (2, "divi", 20, "ECE", 72),
    (3, "loki", 19, "CSE", 90),
    (4, "Divya", 18, "ECE", 95),
    (5, "lokesh", 20, "CME", 68),
    (6, "teja", 19, "CSE", 78),
    (7, "bhavana", 20, "CME", 88),
    (8, "Harsha", 19, "ECE", 60),
    (9, "basheer", 18, "CSE", 92),
    (10, "diya", 20, "CME", 75)
]

cur.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)", data)

con.commit()

print("10 students inserted successfully")

con.close()