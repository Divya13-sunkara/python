import sqlite3

a = sqlite3.connect('mydb.db')

c = a.cursor()

c.execute('DROP TABLE IF EXISTS std')

c.execute('''CREATE TABLE std(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER)''')

data = [
    (1, 'divi', 2),
    (2, 'sai', 3),
    (3, 'divya', 4),
    (4, 'ABC', 5)
]

c.executemany("INSERT INTO std VALUES(?,?,?)", data)

a.commit()

p = c.execute("SELECT * FROM std")


print(data[0])

c.execute("UPDATE std SET id=10 WHERE name='sai'")

a.commit()

print("After UPDATE:")

q = c.execute("SELECT * FROM std")

for i in q:    
    print(i)

b=c.execute("SELECT * FROM std")

print("fetchone():",b.fetchone())

print("fetchmany():",b.fetchmany(2))

print("fetchall():",b.fetchall())

a.close()