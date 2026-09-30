import os

if os.path.exists("students.txt"):
    f = open("students.txt", "r")
    print(f.read())
    f.close()
else:
    print("File does not exist")