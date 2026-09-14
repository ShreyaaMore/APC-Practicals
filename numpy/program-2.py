# 2.	Create two NumPy arrays of 5 integers each. Perform and display:
# •	Addition 
# •	Subtraction 
# •	Multiplication 
# •	Division 
# •	Modulus

import numpy as np

arr1 = np.array([20, 35, 50, 65, 80])
arr2 = np.array([4, 5, 8, 10, 12])

print("Array 1        :", arr1)
print("Array 2        :", arr2)
print("Addition (+)   :", np.add(arr1, arr2))
print("Subtraction (-):", np.subtract(arr1, arr2))
print("Multiplication (*):", np.multiply(arr1, arr2))
print("Division (/)   :", np.divide(arr1, arr2))
print("Modulus (%)    :", np.mod(arr1, arr2))
