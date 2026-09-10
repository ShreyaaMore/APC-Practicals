# 11.	Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, cart_id, customer_name):
        self.cart_id = cart_id
        self.customer_name = customer_name
        self.items = {}
        print(f"ShoppingCart [{self.cart_id}] created for {self.customer_name}.")

    def add_product(self, product_name, price):
        self.items[product_name] = price
        print(f"Added '{product_name}' (Rs. {price:.2f}) to cart.")

    def remove_product(self, product_name):
        if product_name in self.items:
            price = self.items.pop(product_name)
            print(f"Removed '{product_name}' (Rs. {price:.2f}) from cart.")
        else:
            print(f"'{product_name}' not found in cart.")

    def calculate_total(self):
        total = sum(self.items.values())
        return total

    def display_cart(self):
        print(f"\nCart Summary for {self.customer_name}")
        for item, price in self.items.items():
            print(f"- {item}: Rs. {price:.2f}")
        print(f"Total Bill: Rs. {self.calculate_total():.2f}\n")

    def __del__(self):
        print(f"Destructor called: ShoppingCart [{self.cart_id}] for {self.customer_name} is destroyed.")


cart = ShoppingCart("CART101", "Ananya Sen")
cart.add_product("Wireless Earbuds", 2499.0)
cart.add_product("USB-C Hub", 1299.0)
cart.add_product("Laptop Stand", 999.0)
cart.display_cart()
cart.remove_product("USB-C Hub")
cart.display_cart()
del cart
