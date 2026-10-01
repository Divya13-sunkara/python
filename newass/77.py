a = [10, 20, 30, 40]
b = [20, 30, 50]
c = [30, 20, 60]

d = []

for i in a:
    if i in b and i in c:
        d.append(i)

print(d)