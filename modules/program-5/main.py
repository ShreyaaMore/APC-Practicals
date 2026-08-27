# 5.	Create a module containing functions to calculate gross salary, deductions, and net salary for an employee.

import salary_utils

emp_name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Pay: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
allowances = float(input("Enter Other Allowances: "))

pf = float(input("Enter Provident Fund (PF): "))
tax = float(input("Enter Income Tax: "))
other_ded = float(input("Enter Other Deductions: "))

gross = salary_utils.calculate_gross_salary(basic, hra, da, allowances)
deductions = salary_utils.calculate_deductions(pf, tax, other_ded)
net_salary = salary_utils.calculate_net_salary(gross, deductions)

print("\nEmployee Salary Slip")
print(f"Employee Name    : {emp_name}")
print(f"Basic Pay        : {basic:.2f}")
print(f"Gross Salary     : {gross:.2f}")
print(f"Total Deductions : {deductions:.2f}")
print(f"Net Salary       : {net_salary:.2f}")

