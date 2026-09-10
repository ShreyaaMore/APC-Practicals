# 7.	Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Storage : {self.storage} GB")
        print(f"Price   : Rs. {self.price:.2f}")

    def calculate_discounted_price(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        return self.price - discount_amount


phone = MobilePhone("Samsung", "Galaxy S24", 256, 79999.0)
print("Phone Specifications")
phone.display_specs()
discount = 10
print(f"Price after {discount}% discount: Rs. {phone.calculate_discounted_price(discount):.2f}")
