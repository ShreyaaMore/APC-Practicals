# Remove all duplicate elements while preserving the original order.

list1 = [10, 20, 10, 30, 20, 40, 30, 50]

new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

print("Original list:",list1)
print("List after removing duplicates:", new_list)