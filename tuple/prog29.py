# Convert a tuple into a sorted tuple in ascending and descending order.

num = (21, 53, 48, 96, 22, 74, 67, 40, 28, 67)

li = list(num)

li.sort()
print("Tuple sorted in Ascending Order:", tuple(li))

li.sort(reverse=True)
print("Tuple sorted in Descending Order:", tuple(li))