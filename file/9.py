f = open("students.txt", "r")
for i in range(5):
    line = f.readline()
    if line == "":
        break
    print(line, end="")
f.close()