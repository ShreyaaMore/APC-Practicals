# 13.	Create an unsorted NumPy array and display it in:
# •	Ascending order 
# •	Descending order

import numpy as np

arr = np.array([45, 12, 89, 23, 7, 56, 34, 91, 18])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Unsorted Array   :", arr)
print("Ascending Order  :", ascending)
print("Descending Order :", descending)

