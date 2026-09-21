# 6.	Create a dictionary containing:
# Student_ID
# Name
# Department
# Total_Classes
# Classes_Attended
# Create a DataFrame and calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100
# Display students whose attendance is below 75%.

import pandas as pd

data = {
    "Student_ID": [201, 202, 203, 204, 205],
    "Name": ["Aarav", "Diya", "Kabir", "Ishita", "Varun"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [60, 60, 60, 60, 60],
    "Classes_Attended": [52, 41, 38, 55, 43]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Complete Student Attendance Report")
print(df)

print("\nStudents with Attendance Below 75%")
shortage_df = df[df["Attendance_Percentage"] < 75]
print(shortage_df[["Student_ID", "Name", "Department", "Attendance_Percentage"]])

