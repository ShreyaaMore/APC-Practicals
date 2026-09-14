# 24.	Create a 3D array containing integers from 1 to 27. Flatten the array and calculate:
# •	Sum 
# •	Average 
# •	Maximum 
# •	Minimum

import numpy as np

arr_3d = np.arange(1, 28).reshape(3, 3, 3)
flattened = arr_3d.flatten()

print("Flattened 1D Array:\n", flattened)
print("Sum     :", np.sum(flattened))
print("Average :", np.mean(flattened))
print("Maximum :", np.max(flattened))
print("Minimum :", np.min(flattened))

