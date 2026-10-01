a = [10, 20, 10, 30, 10]

old = 10
new = 99

for i in range(len(a)):
    if a[i] == old:
        a[i] = new

print(a)