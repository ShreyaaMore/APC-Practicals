# 7.	Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.

import numpy as np

matA = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matB = np.array([
    [7, 8],
    [9, 1],
    [2, 3]
])

result = np.matmul(matA, matB)

print("Matrix A (2x3):\n", matA)
print("\nMatrix B (3x2):\n", matB)
print("\nMatrix Multiplication (A x B) [2x2]:\n", result)

