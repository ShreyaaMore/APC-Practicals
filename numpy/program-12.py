# 12.	Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.

import numpy as np

arr = np.array([25, 62, 14, 88, 49, 99, 31, 55, 12, 70])
print("Original Array :", arr)

arr[arr > 50] = 0

print("Modified Array (elements > 50 replaced with 0):", arr)

