products = {
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 8,
    "Monitor": 12,
    "Speaker": 6
}
for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)