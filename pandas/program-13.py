# 13.	Dataset: students.csv
# Columns:
# Student_ID,Name,Department,Python,DBMS,Maths
# Problem Statement:
# Read students.csv using Pandas and perform the following:
# 1.	Display the first 5 records. 
# 2.	Display the last 5 records. 
# 3.	Find the total and average marks of each student. 
# 4.	Display students whose average marks are greater than 75. 
# 5.	Find the student with the highest average. 
# 6.	Find the average marks for each subject.

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
df = pd.read_csv(csv_path)

print("1. First 5 Records")
print(df.head(5))

print("\n2. Last 5 Records")
print(df.tail(5))

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("\n3. Total and Average Marks")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\n4. Students with Average > 75")
print(df[df["Average"] > 75][["Student_ID", "Name", "Average"]])

top_student = df.loc[df["Average"].idxmax()]
print(f"\n5. Student with Highest Average: {top_student['Name']} ({top_student['Average']:.2f})")

print("\n6. Average Marks for Each Subject")
subject_averages = df[["Python", "DBMS", "Maths"]].mean()
print(subject_averages.round(2))

