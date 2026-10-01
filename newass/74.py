a = [10, 20, 30, 40]
b = [30, 40, 50, 60]

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)