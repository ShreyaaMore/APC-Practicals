# 2.	Create a module student.py containing functions to calculate total marks, percentage, and grade. Import the module into another Python program and generate a student's result.

import student

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
num_subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(1, num_subjects + 1):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = student.calculate_total(marks)
percentage = student.calculate_percentage(marks)
grade = student.calculate_grade(percentage)

print("\nStudent Result:")
print(f"Name      : {name}")
print(f"Roll No   : {roll_no}")
print(f"Total     : {total:.2f} / {num_subjects * 100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade     : {grade}")

