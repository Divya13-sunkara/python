import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.xticks(rotation=45)
plt.yticks([0, 20, 40, 60, 80, 100])

plt.show()