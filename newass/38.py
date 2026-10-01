a = [10, 20, 10, 30, 10]

n = 10
new = 99

i = 0

while i < len(a):
    if a[i] == n:
        a.insert(i + 1, new)
        i += 1
    i += 1

print(a)