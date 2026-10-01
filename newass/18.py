a = [10, 50, 30, 40, 20]

smallest = a[0]
second = a[0]

for i in a:
    if i < smallest:
        second = smallest
        smallest = i
    elif i < second and i != smallest:
        second = i

print(second)