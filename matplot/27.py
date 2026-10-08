import matplotlib.pyplot as plt

class_a = [40, 45, 50, 55, 60]
class_b = [50, 55, 60, 65, 70]

plt.hist(class_a, bins=5, alpha=0.5, label="Class A")
plt.hist(class_b, bins=5, alpha=0.5, label="Class B")

plt.legend()
plt.show()