# 19.	Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

products = {
    "apple": 189.0,
    "cherry": 159.0,
    "banana": 59.0,
    "mango": 259.0,
    "coconut": 80.0,
    "chicko": 89.0,
    "pineapple": 159.0,
}

print("Products:", products)
temp = products.copy()
values = []

for product, price in temp.items():
    if price in values:
        products.pop(product)
    else:
        values.append(price)
        
print("Update Products:", products)