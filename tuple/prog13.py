# Modify a tuple by converting it into a list and then back into a tuple.

fruits = ("Apple", "Banana", "Cherry", "Grapes", "Guava")

li = list(fruits)

li.extend(["Mango","Watermelon"])

print("Modified tuple:", tuple(li))