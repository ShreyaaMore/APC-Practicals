# Merge two tuples and remove duplicate elements.

t1 = ("Apple", "Cherry", "Strawberry", "Banana")
t2 = ("Guava", "Banana", "Kiwi", "Pineapple", "Cherry")

t = t1 + t2
result = set(t)

print("Merged tuple:",t)
print("Tuple without duplicates:",tuple(result))