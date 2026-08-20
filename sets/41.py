marks = {
    "Ravi": 85,
    "Anu": 72,
    "Kiran": 90,
    "Priya": 68,
    "Rahul": 80
}
for student, mark in marks.items():
    if mark > 75:
        print(student, mark)