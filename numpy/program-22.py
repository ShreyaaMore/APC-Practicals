# 22.	Generate a random 3D array of shape (3, 4, 5) and calculate its:
# mean, median, standard deviation, variance, minimum, and maximum.

import numpy as np

np.random.seed(10)
arr = np.random.randint(1, 100, size=(3, 4, 5))

print(f"Random 3D Array generated with shape: {arr.shape} and size: {arr.size}")
print(f"Mean               : {np.mean(arr):.2f}")
print(f"Median             : {np.median(arr):.2f}")
print(f"Standard Deviation : {np.std(arr):.2f}")
print(f"Variance           : {np.var(arr):.2f}")
print(f"Minimum            : {np.min(arr)}")
print(f"Maximum            : {np.max(arr)}")

