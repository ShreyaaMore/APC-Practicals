# 12.	Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        print(f"Order #{self.order_id} placed by {self.customer_name}.")

    def calculate_total_bill(self, tax_rate=5.0):
        subtotal = self.quantity * self.price
        tax = subtotal * (tax_rate / 100)
        total = subtotal + tax
        return subtotal, tax, total

    def display_order_details(self):
        subtotal, tax, total = self.calculate_total_bill()
        print(f"\nOrder Details (#{self.order_id})")
        print(f"Customer Name : {self.customer_name}")
        print(f"Food Item     : {self.food_item}")
        print(f"Quantity      : {self.quantity}")
        print(f"Price/Unit    : Rs. {self.price:.2f}")
        print(f"Subtotal      : Rs. {subtotal:.2f}")
        print(f"GST (5%)      : Rs. {tax:.2f}")
        print(f"Total Bill    : Rs. {total:.2f}\n")

    def __del__(self):
        print(f"Destructor: Food order #{self.order_id} for {self.customer_name} has been completed and closed.")


order = FoodOrder("FD-401", "Rohan Gupta", "Paneer Butter Masala Combo", 2, 280.0)
order.display_order_details()
del order
