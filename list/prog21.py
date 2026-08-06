# Accept two lists and merge them into a single list.


list1 = []
list2 = []

n1 = int(input("Enter no. of items in list 1: "))
n2 = int(input("Enter no. of items in list 2: "))

for i in range(n1):
    item = input("Enter an item in list 1: ")
    list1.append(item)

for i in range(n2):
    item = input("Enter an item in list 2: ")
    list2.append(item)
    
merged = list1 + list2
print("Merged list:",merged)