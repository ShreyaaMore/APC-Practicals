# 27. Create a dictionary containing product names and quantities.
# Perform: • Add a product 
# • Update quantity 
# • Delete a product 
# • Search for a product 
# • Display products with quantity below 10

products = {
    "Apple": 50, 
    "Banana": 5, 
    "Orange": 12, 
    "Mango": 8
}

def add_product(name, quantity):
    products[name] = quantity
    print(f"Added product {name}.")

def update_quantity(name, quantity):
    if name in products:
        products[name] = quantity
        print(f"Updated quantity for {name}.")
    else:
        print(f"Product {name} not found.")

def delete_product(name):
    if name in products:
        del products[name]
        print(f"Deleted product {name}.")
    else:
        print(f"Product {name} not found.")

def search_product(name):
    if name in products:
        print(f"Product: {name}, Quantity: {products[name]}")
    else:
        print(f"Product {name} not found.")

def display_low_stock():
    print("Products with quantity below 10:")
    for name, quantity in products.items():
        if quantity < 10:
            print(f"{name}: {quantity}")


print("Initial products:", products)
add_product("Grapes", 15)
update_quantity("Apple", 45)
delete_product("Orange")
search_product("Banana")
display_low_stock()
