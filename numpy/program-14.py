# 14.	Create an array containing duplicate values. Find and display only the unique elements.

import numpy as np

arr = np.array([10, 20, 20, 30, 40, 10, 50, 30, 60, 40, 70])

unique_elements = np.unique(arr)

print("Array with duplicates :", arr)
print("Unique elements       :", unique_elements)

