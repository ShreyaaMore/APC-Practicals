# 25.	Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:
# •	Greater than 50 
# •	Even numbers 
# •	Less than the average value

import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened = arr.flatten()
avg_val = np.mean(flattened)

gt_50 = flattened[flattened > 50]
even_nums = flattened[flattened % 2 == 0]
lt_avg = flattened[flattened < avg_val]

print(f"Flattened Array ({flattened.size} elements):\n", flattened)
print(f"\nAverage value of elements: {avg_val:.2f}")
print("\nElements Greater than 50:\n", gt_50)
print("\nEven Numbers:\n", even_nums)
print(f"\nElements Less than Average ({avg_val:.2f}):\n", lt_avg)

