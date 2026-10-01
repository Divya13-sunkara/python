a = [10, 20, 10, 30, 10, 20]

most = a[0]

for i in a:
    if a.count(i) > a.count(most):
        most = i

print(most)