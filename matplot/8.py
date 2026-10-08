import matplotlib.pyplot as plt
marks=[80, 90, 70, 85, 95]
plt.hist(marks, bins=10, edgecolor='red')
plt.title('mark')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()