# 1.	Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes and override the area() method in each class. Create objects of each class and demonstrate runtime polymorphism.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(6, 8)
]

print("Runtime Polymorphism with Shapes")
for s in shapes:
    print(f"Shape: {s.__class__.__name__:<10} | Area: {s.area():.2f}")
