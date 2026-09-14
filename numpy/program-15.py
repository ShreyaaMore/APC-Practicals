# 15.	Create two NumPy arrays and concatenate them horizontally and vertically. 

import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

concat_h = np.hstack((arr1, arr2))

concat_v = np.vstack((arr1, arr2))

print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)
print("\nHorizontal Concatenation (hstack):\n", concat_h)
print("\nVertical Concatenation (vstack):\n", concat_v)

