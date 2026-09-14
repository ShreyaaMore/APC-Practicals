# 18.	Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its:
# •	Number of dimensions 
# •	Shape 
# •	Size

import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array (2, 3, 4):\n", arr_3d)
print("\nNumber of dimensions :", arr_3d.ndim)
print("Shape                :", arr_3d.shape)
print("Size (total elements):", arr_3d.size)

