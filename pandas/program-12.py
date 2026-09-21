# 12.	Create a Pandas Series using a dictionary containing student names and attendance percentages.
# Perform:
# •	Find the average attendance. 
# •	Display students with attendance below 75%. 
# •	Display students with attendance above 90%. 
# •	Find the highest attendance.

import pandas as pd

attendance_data = {
    "Amit": 82.5,
    "Bhavna": 71.0,
    "Chetan": 94.0,
    "Divya": 68.5,
    "Esha": 91.5,
    "Farhan": 78.0,
    "Gauri": 96.0
}

att = pd.Series(attendance_data)

print("Student Attendance Series (%)")
print(att)

print(f"\nAverage Attendance : {att.mean():.2f}%")

print(f"Highest Attendance : {att.max()}% ({att.idxmax()})")

print("\nStudents with Attendance Below 75%")
print(att[att < 75.0])

print("\nStudents with Attendance Above 90%")
print(att[att > 90.0])

