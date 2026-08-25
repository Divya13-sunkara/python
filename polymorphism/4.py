class Student:
    def display(self):
        print("Student details")

class Teacher:
    def display(self):
        print("Teacher details")

for person in [Student(), Teacher()]:
    person.display()