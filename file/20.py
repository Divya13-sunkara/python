f = open("student.txt", "w")
f.write("Name: Divya\n")
f.write("Marks: 95\n")
f.close()

f = open("student.txt", "r")
print(f.read())
f.close()

f = open("student.txt", "a")
f.write("Grade: A\n")
f.close()