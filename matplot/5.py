import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°F)")
plt.show()