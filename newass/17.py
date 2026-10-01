a = [10, 50, 30, 40, 20]

largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)