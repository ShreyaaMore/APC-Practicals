# 17.	Given two dictionaries, find the keys that are common to both dictionaries.

products_A = {
    "apple": 189.0,
    "cherry": 159.0,
    "banana": 59.0,
    "mango": 259.0,
    "coconut": 80.0
}


products_B = {
    "apple": 189.0,
    "cherry": 159.0,
    "chicko": 89.0,
    "pineapple": 156.0,
    "bambo": 800.0
}

common = []
for product in products_A:
    if product in products_B:
        common.append(product)

print("Products A:", products_A)
print("Products B:", products_B)
print("Common Products:", common)