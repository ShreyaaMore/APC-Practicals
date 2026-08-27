# 20.	Create a dictionary and display its elements in ascending order of keys.

products = {
    "apple": 189.0,
    "cherry": 159.0,
    "banana": 59.0,
    "mango": 259.0,
    "coconut": 80.0,
    "chicko": 89.0,
    "pineapple": 159.0,
}
print("Dictionary:", products)

elements = list(product for product in products)
elements.sort()
sorted_products = {}

for product in elements:
    sorted_products[product] = products[product]

print("Sorted Dictionary:",  sorted_products)