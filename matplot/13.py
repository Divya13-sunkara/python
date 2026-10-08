import matplotlib.pyplot as plt
products=['laptop','mobile','tablet','desktop']
sales=[100,200,150,300]
plt.fill_between(products,sales)
plt.title("Product Sales")
plt.xlabel("Products")  
plt.ylabel("Sales")
plt.show()