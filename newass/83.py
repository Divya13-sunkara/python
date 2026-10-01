a = [10, 20, 10, 30, 20, 10]

least = a[0]

for i in a:
    if a.count(i) < a.count(least):
        least = i

print(least)