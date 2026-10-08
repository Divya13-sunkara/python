import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.savefig("chart.png", dpi=300, bbox_inches="tight")

plt.show()