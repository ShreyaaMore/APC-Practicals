from array import array

arr = array('i', [50, 40, 10, 30, 20])
print("Array:", arr)

arr.pop()
print("Array after pop:", arr)

arr.remove(10)
print("Array after removing 10:", arr)