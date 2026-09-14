# 8.	Create a 3 × 4 matrix and display its transpose.

import numpy as np

mat = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

transpose_mat = mat.T

print("Original 3x4 Matrix:\n", mat)
print("\nTransposed 4x3 Matrix:\n", transpose_mat)

