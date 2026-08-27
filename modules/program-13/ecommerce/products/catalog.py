"""Products catalog module."""

products = {
    "P101": {"name": "Laptop", "category": "Electronics", "price": 55000.0},
    "P102": {"name": "Wireless Mouse", "category": "Accessories", "price": 1200.0},
    "P103": {"name": "Mechanical Keyboard", "category": "Accessories", "price": 3500.0}
}

def get_product(pid):
    return products.get(pid)

def list_products():
    return products

