# 23.	Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.

import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)
flattened = arr_3d.flatten()

print("Original 3D Array (shape 2, 3, 4):\n", arr_3d)
print("\nFlattened 1D Array:\n", flattened)
print(f"Original shape: {arr_3d.shape} -> Flattened shape: {flattened.shape}")

