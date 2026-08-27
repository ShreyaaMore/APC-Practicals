# 8.	Create a package student containing:
# a)	marks.py – total and percentage 
# b)	grade.py – grade calculation 
# c)	attendance.py – attendance eligibility 
# Write a main program that uses all three modules to generate a student report.

from student.marks import calculate_total, calculate_percentage
from student.grade import calculate_grade
from student.attendance import calculate_attendance_percentage, check_eligibility

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

marks = [85, 92, 78, 88, 90]
total_classes = 60
classes_attended = 48

total = calculate_total(marks)
percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

att_pct = calculate_attendance_percentage(classes_attended, total_classes)
eligible = check_eligibility(classes_attended, total_classes)

print("\nSTUDENT REPORT:")
print(f"Name                  : {name}")
print(f"Roll Number           : {roll_no}")
print(f"Marks Obtained        : {marks}")
print(f"Total Marks           : {total} / {len(marks) * 100}")
print(f"Academic Percentage   : {percentage:.2f}%")
print(f"Final Grade           : {grade}")
print(f"Attendance            : {classes_attended}/{total_classes} ({att_pct:.2f}%)")
print(f"Exam Eligibility      : {'Eligible' if eligible else 'Not Eligible (Attendance shortage)'}")
print()

