salaries = {
    "Ravi": 45000,
    "Anu": 55000,
    "Kiran": 60000,
    "Priya": 50000
}
total = 0
for salary in salaries.values():
    total += salary
average = total / len(salaries)
print(average)