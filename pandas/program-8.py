# 8.	Create a Pandas Series using a dictionary where the student names are keys and their marks are values.
# Perform:
# •	Display the Series. 
# •	Display marks of a particular student. 
# •	Find maximum and minimum marks. 
# •	Calculate the average marks. 
# •	Display students who scored more than 75. 

import pandas as pd

student_marks = {
    "Amit": 82,
    "Priya": 91,
    "Rahul": 68,
    "Sneha": 74,
    "Shreya": 95,
    "Ananya": 88
}

s = pd.Series(student_marks)

print("Student Marks Series")
print(s)

student_name = "Shreya"
print(f"\nMarks of '{student_name}': {s[student_name]}")

print(f"Maximum Marks : {s.max()} (by {s.idxmax()})")
print(f"Minimum Marks : {s.min()} (by {s.idxmin()})")

print(f"Average Marks : {s.mean():.2f}")

print("\nStudents Scoring More Than 75")
print(s[s > 75])

