# 14.	Dataset: employees.csv
# Columns:
# Employee_ID,Name,Department,Experience,Salary
# Problem Statement:
# Read the CSV file and:
# 1.	Display employees from the CSE department. 
# 2.	Find the average salary. 
# 3.	Find the highest and lowest salary. 
# 4.	Display employees having salary greater than ₹50,000. 
# 5.	Calculate department-wise average salary.

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "employees.csv")
df = pd.read_csv(csv_path)

print("Employee Dataset")
print(df)

print("\n1. Employees from CSE Department")
print(df[df["Department"] == "CSE"])

print(f"\n2. Average Salary: ₹{df['Salary'].mean():,.2f}")

print(f"\n3. Salary Extremes")
print(f"Highest Salary : ₹{df['Salary'].max():,d}")
print(f"Lowest Salary  : ₹{df['Salary'].min():,d}")

print("\n4. Employees with Salary > ₹50,000")
print(df[df["Salary"] > 50000])

print("\n5. Department-wise Average Salary")
dept_avg = df.groupby("Department")["Salary"].mean()
print(dept_avg.apply(lambda x: f"₹{x:,.2f}"))

