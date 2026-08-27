"""Shopping cart module."""

def create_cart():
    return []

def add_to_cart(cart, product, quantity=1):
    cart.append({"product": product, "quantity": quantity})
    return cart

def get_cart_total(cart):
    return sum(item["product"]["price"] * item["quantity"] for item in cart)

