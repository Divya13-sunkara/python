a = [10, 20, 10, 30, 20, 40]

b = []

for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)

print(b)