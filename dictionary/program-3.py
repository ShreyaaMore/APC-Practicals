# 3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.

products = {
    "apple": 189.0,
    "cherry": 159.0,
    "banana": 59.0,
    "mango": 259.0,
    "coconut": 80.0
}

print("Products:", products)

products["berry"] = 99.0

print(f"Added product Berry with price {products["berry"]}")
print("Products:", products)