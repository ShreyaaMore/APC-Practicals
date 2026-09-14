# 19.	Create a 3D array of shape (2, 3, 4) and write a program to access:
# •	First element 
# •	Last element 
# •	Element at index [0,1,2] 
# •	Element at index [1,2,3]

import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr_3d)
print("\nFirst element [0, 0, 0]      :", arr_3d[0, 0, 0])
print("Last element [-1, -1, -1]    :", arr_3d[-1, -1, -1])
print("Element at index [0, 1, 2]   :", arr_3d[0, 1, 2])
print("Element at index [1, 2, 3]   :", arr_3d[1, 2, 3])

