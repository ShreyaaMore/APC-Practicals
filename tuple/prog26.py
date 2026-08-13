# Create two tuples and find the common elements between them.

t1 = (101,55,43,220,74,62,35,41)
t2 = (52,43,62,220,110,55,34,98)

common = []

for i in t1:
    if i in t2:
        common.append(i)

print("The common elements is:",common)