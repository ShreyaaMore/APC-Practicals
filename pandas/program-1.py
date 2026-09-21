# 1.	Create a dictionary containing the following information for 5 students:
# •	Student ID 
# •	Student Name 
# •	Python Marks 
# •	DBMS Marks 
# •	Mathematics Marks 
# Convert the dictionary into a Pandas DataFrame and:
# 1.	Display the DataFrame. 
# 2.	Calculate total marks for each student. 
# 3.	Calculate average marks. 
# 4.	Display students who scored more than 75% average.

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Shreya"],
    "Python_Marks": [85, 92, 65, 78, 95],
    "DBMS_Marks": [78, 88, 70, 82, 90],
    "Mathematics_Marks": [90, 95, 60, 74, 92]
}

df = pd.DataFrame(data)

print("1. Original DataFrame")
print(df)

df["Total_Marks"] = df["Python_Marks"] + df["DBMS_Marks"] + df["Mathematics_Marks"]
print("\n2. With Total Marks")
print(df[["Student_ID", "Student_Name", "Total_Marks"]])

df["Average_Marks"] = df["Total_Marks"] / 3
print("\n3. With Average Marks")
print(df[["Student_ID", "Student_Name", "Total_Marks", "Average_Marks"]])

print("\n4. Students Scored More Than 75% Average")
high_achievers = df[df["Average_Marks"] > 75]
print(high_achievers[["Student_ID", "Student_Name", "Average_Marks"]])

