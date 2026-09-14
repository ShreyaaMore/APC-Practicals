# 17.	Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.

import numpy as np

marks = np.array([55, 78, 88, 92, 45, 67, 85, 90, 72, 60,
                  81, 79, 95, 68, 74, 83, 89, 62, 70, 96])

class_average = np.mean(marks)
above_average_marks = marks[marks > class_average]

print(f"Marks of 20 Students : {marks}")
print(f"Class Average        : {class_average:.2f}")
print(f"Marks Above Average  : {above_average_marks}")
print(f"Count Above Average  : {len(above_average_marks)}")

