numbers = {10, 50, 30, 80, 20}
smallest = None
for n in numbers:
    if smallest is None or n < smallest:
        smallest = n
print(smallest)