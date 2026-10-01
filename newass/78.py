a = [10, 20, 30]
b = [20, 30, 40]

c = []

for i in a + b:
    if i not in c:
        c.append(i)

print(c)