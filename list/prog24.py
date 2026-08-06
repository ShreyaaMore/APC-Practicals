#   Rotate a list:
# •	Left by one position 
# •	Right by one position

list1 = [10, 20, 30, 40, 50]

first = list1.pop(0)
list1.append(first)

print("List after left rotation:", list1)

last = list1.pop()
list1.insert(0, last)

print("List after right rotation:", list1)