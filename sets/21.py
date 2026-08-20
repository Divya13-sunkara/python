numbers = {10, 50, 30, 80, 20}
largest = None
for n in numbers:
    if largest is None or n > largest:
        largest = n
print(largest)