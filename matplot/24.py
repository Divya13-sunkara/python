import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]

plt.plot(months, sales)

plt.savefig("sales_chart.png")

plt.show()