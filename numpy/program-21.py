# 21.	Create a 3D array of random integers between 1 and 100. Replace all values greater than 50 with 0

import numpy as np

np.random.seed(42)

arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Random 3D Array:\n", arr)

arr[arr > 50] = 0

print("\nModified 3D Array (values > 50 replaced with 0):\n", arr)

