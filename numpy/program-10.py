# 10.	Create a 4 × 4 matrix and calculate the sum of each row and each column separately.

import numpy as np

mat = np.array([
    [10, 20, 30, 40],
    [5,  15, 25, 35],
    [2,   4,  6,  8],
    [1,   3,  5,  7]
])

row_sum = np.sum(mat, axis=1)
col_sum = np.sum(mat, axis=0)

print("4x4 Matrix:\n", mat)
print("\nSum of each row (axis=1)   :", row_sum)
print("Sum of each column (axis=0):", col_sum)

