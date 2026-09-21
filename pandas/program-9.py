# 9.	Create a Pandas Series using a dictionary containing employee names and their salaries.
# Perform:
# •	Display the Series. 
# •	Find the highest salary. 
# •	Find the lowest salary. 
# •	Calculate average salary. 
# •	Display employees earning more than ₹50,000.

import pandas as pd

employee_salaries = {
    "Rajesh": 65000,
    "Meera": 48000,
    "Vikas": 82000,
    "Pooja": 52000,
    "Arjun": 45000,
    "Neha": 71000
}

salary_series = pd.Series(employee_salaries)

print("Employee Salaries Series")
print(salary_series)

print(f"\nHighest Salary : ₹{salary_series.max():,d} ({salary_series.idxmax()})")
print(f"Lowest Salary  : ₹{salary_series.min():,d} ({salary_series.idxmin()})")

print(f"Average Salary : ₹{salary_series.mean():,.2f}")

print("\nEmployees Earning More Than ₹50,000")
print(salary_series[salary_series > 50000])

