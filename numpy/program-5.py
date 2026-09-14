# 5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
# •	2 × 6 matrix 
# •	3 × 4 matrix 
# •	4 × 3 matrix

import numpy as np

arr = np.arange(1, 13)

matrix_2x6 = arr.reshape(2, 6)
matrix_3x4 = arr.reshape(3, 4)
matrix_4x3 = arr.reshape(4, 3)

print("Original 1D Array:\n", arr)
print("\n2 x 6 Matrix:\n", matrix_2x6)
print("\n3 x 4 Matrix:\n", matrix_3x4)
print("\n4 x 3 Matrix:\n", matrix_4x3)

