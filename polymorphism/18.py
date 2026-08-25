class Person:
    def role(self):
        print("Person")

class Student(Person):
    def role(self):
        print("Student studies")

class Teacher(Person):
    def role(self):
        print("Teacher teaches")

class Doctor(Person):
    def role(self):
        print("Doctor treats patients")

for person in [Student(), Teacher(), Doctor()]:
    person.role()