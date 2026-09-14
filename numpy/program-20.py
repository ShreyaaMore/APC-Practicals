# 20.	Create a (2, 3, 4) array and calculate:
# •	Sum of all elements 
# •	Sum of each layer 
# •	Sum along rows 
# •	Sum along columns

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

total_sum = np.sum(arr)
layer_sum = np.sum(arr, axis=(1, 2))
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=2)

print("3D Array (2, 3, 4):\n", arr)
print("\nSum of all elements :", total_sum)
print("Sum of each layer (axis=(1,2)) :\n", layer_sum)
print("\nSum along rows (axis=1):\n", row_sum)
print("\nSum along columns (axis=2):\n", col_sum)

