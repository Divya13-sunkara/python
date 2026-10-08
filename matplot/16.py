import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B") 
plt.legend() 
plt.show()