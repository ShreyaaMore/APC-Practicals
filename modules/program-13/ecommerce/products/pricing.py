"""Product pricing and discounts module."""

def calculate_discounted_price(price, discount_percent):
    return price * (1 - discount_percent / 100)

def calculate_tax(amount, tax_rate=18.0):
    return amount * (tax_rate / 100)

