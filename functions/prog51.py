products = [
    {"name": "Laptop", "price": 50000, "qty": 2},
    {"name": "Mouse", "price": 500, "qty": 10},
    {"name": "Keyboard", "price": 1200, "qty": 5},
    {"name": "Monitor", "price": 8000, "qty": 3},
    {"name": "Pen", "price": 20, "qty": 50}
]

def calculate_total_values(prods):
    return list(map(lambda p: {**p, "total_value": p["price"] * p["qty"]}, prods))

products_with_total = calculate_total_values(products)
print("Products with total value:", products_with_total)

costly_products = list(filter(lambda p: p["price"] > 1000, products))
print("Products costing > 1000:", costly_products)

sorted_by_total = sorted(products_with_total, key=lambda p: p["total_value"])
print("Products sorted by total value:", sorted_by_total)
