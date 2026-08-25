class Rectangle:
    def area(self):
        print("Rectangle area:", 10 * 5)

class Circle:
    def area(self):
        print("Circle area:", 3.14 * 4 * 4)

class Triangle:
    def area(self):
        print("Triangle area:", 0.5 * 10 * 6)

def calculate_area(shape):
    shape.area()

calculate_area(Rectangle())
calculate_area(Circle())
calculate_area(Triangle())