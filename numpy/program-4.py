# 4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.

import numpy as np

arr = np.arange(1, 21)

even_numbers = arr[arr % 2 == 0]
odd_numbers = arr[arr % 2 != 0]

print("Original Array :", arr)
print("Even Numbers   :", even_numbers)
print("Odd Numbers    :", odd_numbers)

