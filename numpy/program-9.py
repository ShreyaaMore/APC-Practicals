# 9.	Create a 4 × 4 NumPy array and write a program to:
# •	Display the first row 
# •	Display the last column 
# •	Display the diagonal elements 
# •	Display the elements from the second and third rows

import numpy as np

mat = np.arange(1, 17).reshape(4, 4)

print("4x4 Matrix:\n", mat)
print("\nFirst row:\n", mat[0, :])
print("\nLast column:\n", mat[:, -1])
print("\nDiagonal elements:\n", np.diagonal(mat))
print("\nElements from second and third rows:\n", mat[1:3, :])

