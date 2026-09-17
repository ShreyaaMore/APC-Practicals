# 7.	Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Shape: {self.name}")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
c.display_name()
print(f"Area of Circle: {c.calculate_area():.2f}\n")

r = Rectangle(8, 6)
r.display_name()
print(f"Area of Rectangle: {r.calculate_area():.2f}\n")

t = Triangle(10, 4)
t.display_name()
print(f"Area of Triangle: {t.calculate_area():.2f}\n")
