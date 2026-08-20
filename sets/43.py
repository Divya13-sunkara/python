employees = {
    "Ravi": 45000,
    "Anu": 60000,
    "Kiran": 75000,
    "Priya": 48000,
    "Rahul": 55000
}
for employee, salary in employees.items():
    if salary > 50000:
        print(employee, salary)