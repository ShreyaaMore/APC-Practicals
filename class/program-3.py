# 3.	Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print(f"Length    : {self.length}")
        print(f"Breadth   : {self.breadth}")
        print(f"Area      : {self.area()}")
        print(f"Perimeter : {self.perimeter()}\n")


rect = Rectangle(12, 8)
rect.display()
