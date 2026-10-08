import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 115, 140, 160, 155]

plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()
plt.legend()

plt.show()