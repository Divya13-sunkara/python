import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 130, 180, 210, 190],
    "Orders": [40, 45, 42, 55, 62, 58]
})

# Sales Trend
plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()


# Sales Comparison
plt.bar(df["Month"], df["Sales"])

plt.title("Monthly Sales Comparison")

plt.show()


# Orders Distribution
plt.hist(df["Orders"], bins=4)

plt.title("Orders Distribution")
plt.xlabel("Orders")
plt.ylabel("Frequency")

plt.show()

plt.scatter(df["Orders"], df["Sales"])

plt.title("Orders vs Sales")
plt.xlabel("Orders")
plt.ylabel("Sales")

plt.show()