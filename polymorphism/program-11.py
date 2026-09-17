# 11.	Create a class Product with product name and price. Overload the == and > operators to compare two products based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __str__(self):
        return f"{self.name} (Rs. {self.price:.2f})"


p1 = Product("Logitech MX Master 3S", 8995.0)
p2 = Product("Apple Magic Mouse", 8500.0)
p3 = Product("Razer DeathAdder", 8500.0)

print("Operator Overloading: Product Price Comparison (== and >)")
print(f"Product 1 : {p1}")
print(f"Product 2 : {p2}")
print(f"Product 3 : {p3}\n")

print(f"Is {p1.name} more expensive than {p2.name}? -> {p1 > p2}")
print(f"Is {p2.name} priced identically to {p3.name}? -> {p2 == p3}")
