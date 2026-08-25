class Rectangle:
    def area(self):
        print("Rectangle area:", 10 * 5)

class Circle:
    def area(self):
        print("Circle area:", 3.14 * 4 * 4)

for shape in [Rectangle(), Circle()]:
    shape.area()