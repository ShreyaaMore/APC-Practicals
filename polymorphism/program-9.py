# 9.	Create a class Distance with feet and inches. Overload the + operator to add two distance objects and display the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        if self.inches >= 12:
            self.feet += int(self.inches // 12)
            self.inches = self.inches % 12

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        return Distance(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} ft {self.inches} in"


d1 = Distance(5, 9)
d2 = Distance(3, 8)
d3 = d1 + d2

print("Operator Overloading: Distance Addition")
print(f"Distance 1 : {d1}")
print(f"Distance 2 : {d2}")
print(f"Sum (+ op) : {d3}")
