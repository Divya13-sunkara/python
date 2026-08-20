marks = {
    "Ravi": 85,
    "Anu": 92,
    "Kiran": 78,
    "Priya": 88
}
highest = 0
topper = ""
for student, mark in marks.items():
    if mark > highest:
        highest = mark
        topper = student
print(topper)
print(highest)