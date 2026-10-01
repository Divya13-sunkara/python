a = [10, 20, 30, 40, 50]

temp = a[0]
a[0] = a[-1]
a[-1] = temp

print(a)