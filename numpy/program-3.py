# 3.	Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.

import numpy as np

arr = np.array([45, 12, 89, 34, 76, 23, 98, 56, 67, 10])

print("Array   :", arr)
print("Maximum :", np.max(arr))
print("Minimum :", np.min(arr))
print("Sum     :", np.sum(arr))
print("Average :", np.mean(arr))
