# 2.	Create a dictionary containing:
# Employee ID
# Employee Name
# Department
# Salary
# Experience
# Convert it into a Pandas DataFrame and:
# 1.	Display employees with salary greater than ₹50,000. 
# 2.	Find the average salary. 
# 3.	Find the highest salary. 
# 4.	Find the employee with the highest experience.

import pandas as pd

data = {
    "Employee_ID": ["E101", "E102", "E103", "E104", "E105"],
    "Employee_Name": ["Rajesh", "Pooja", "Vikram", "Ananya", "Suresh"],
    "Department": ["IT", "HR", "IT", "Finance", "Operations"],
    "Salary": [65000, 48000, 82000, 52000, 45000],
    "Experience": [5, 3, 8, 4, 2]
}

df = pd.DataFrame(data)

print("Employee DataFrame")
print(df)

print("\n1. Employees with Salary > ₹50,000")
print(df[df["Salary"] > 50000])

avg_salary = df["Salary"].mean()
print(f"\n2. Average Salary: ₹{avg_salary:,.2f}")

highest_salary = df["Salary"].max()
print(f"\n3. Highest Salary: ₹{highest_salary:,.2f}")

max_exp_row = df.loc[df["Experience"].idxmax()]
print(f"\n4. Employee with Highest Experience ({max_exp_row['Experience']} years)")
print(f"Name: {max_exp_row['Employee_Name']}, ID: {max_exp_row['Employee_ID']}, Department: {max_exp_row['Department']}")

