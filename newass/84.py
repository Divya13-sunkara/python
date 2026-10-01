a = [2, 4, 3, 5, 7, 8]
n = 10

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == n:
            print(a[i], a[j])