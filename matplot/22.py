import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(months, sales)
axes[0, 0].set_title("Line")

axes[0, 1].bar(months, sales)
axes[0, 1].set_title("Bar")

axes[1, 0].hist(sales)
axes[1, 0].set_title("Histogram")

axes[1, 1].scatter(range(4), sales)
axes[1, 1].set_title("Scatter")

plt.tight_layout()
plt.show()