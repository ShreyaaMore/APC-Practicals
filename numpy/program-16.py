# 16.	Store marks of 10 students in a NumPy array. Calculate:
# •	Highest marks 
# •	Lowest marks 
# •	Average marks 
# •	Median 
# •	Standard deviation

import numpy as np

marks = np.array([78, 85, 92, 65, 88, 72, 95, 60, 84, 90])

print("Student Marks      :", marks)
print("Highest Marks      :", np.max(marks))
print("Lowest Marks       :", np.min(marks))
print("Average Marks      :", np.mean(marks))
print("Median             :", np.median(marks))
print(f"Standard Deviation : {np.std(marks):.2f}")

