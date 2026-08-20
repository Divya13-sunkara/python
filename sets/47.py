marks = {
    "Ravi": 85,
    "Anu": 92,
    "Kiran": 68,
    "Priya": 78,
    "Rahul": 75
}
highest = -1
lowest = 101
topper = ""
lowest_scorer = ""
for student, mark in marks.items():
    if mark > highest:
        highest = mark
        topper = student
    if mark < lowest:
        lowest = mark
        lowest_scorer = student
print("Topper:", topper, highest)
print("Lowest Scorer:", lowest_scorer, lowest)