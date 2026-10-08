import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("My Chart")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()
plt.show()