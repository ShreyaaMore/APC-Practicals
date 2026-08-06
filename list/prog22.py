# Find Common Elements Between Two Lists

list1 = []
list2 = []

n1 = int(input("Enter number of elements in list 1: "))
n2 = int(input("Enter number of elements in list 2: "))

for i in range(n1):
    item = int(input("Enter element in list 1: "))
    list1.append(item)

for i in range(n2):
    item = int(input("Enter element in list 2: "))
    list2.append(item)

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common elements are:", common)