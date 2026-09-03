# 18.	Store employee ID, name, department, and salary in a file. Write functions to: 
# •	Display all employees. 
# •	Find the highest-paid employee. 
# •	Calculate average salary. 
# •	Display employees earning above a given salary.

import os

filename = "employees.txt"

def initialize_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("EmpID,Name,Department,Salary\n")
            f.write("E101,Rajesh,IT,65000\n")
            f.write("E102,Sneha,HR,55000\n")
            f.write("E103,Vikas,Finance,72000\n")
            f.write("E104,Ananya,IT,80000\n")
            f.write("E106,Shreya,Engineering,90000\n")

def read_employees(file_name):
    employees = []
    with open(file_name, "r") as f:
        f.readline()
        for line in f:
            line = line.strip()
            if line:
                emp_id, name, dept, salary = line.split(",")
                employees.append({
                    "id": emp_id,
                    "name": name,
                    "dept": dept,
                    "salary": float(salary)
                })
    return employees

def display_all_employees(file_name):
    employees = read_employees(file_name)
    print("\nEmployee Records:")
    print(f"{'ID':<10} {'Name':<15} {'Department':<15} {'Salary':<10}")
    print()
    for emp in employees:
        print(f"{emp['id']:<10} {emp['name']:<15} {emp['dept']:<15} {emp['salary']:<10.2f}")

def find_highest_paid_employee(file_name):
    employees = read_employees(file_name)
    if not employees:
        print("No employees found.")
        return
    highest = max(employees, key=lambda e: e["salary"])
    print(f"\nHighest-Paid Employee: {highest['name']} (ID: {highest['id']}, Salary: {highest['salary']:.2f})")

def calculate_average_salary(file_name):
    employees = read_employees(file_name)
    if not employees:
        print("No employees found.")
        return
    avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
    print(f"\nAverage Salary: {avg_salary:.2f}")

def display_employees_above_salary(file_name, threshold):
    employees = read_employees(file_name)
    print(f"\nEmployees earning above {threshold:.2f}:")
    found = False
    for emp in employees:
        if emp["salary"] > threshold:
            print(f"- {emp['name']} (ID: {emp['id']}, Dept: {emp['dept']}, Salary: {emp['salary']:.2f})")
            found = True
    if not found:
        print("No employee earns above this amount.")

initialize_file(filename)
display_all_employees(filename)
find_highest_paid_employee(filename)
calculate_average_salary(filename)

salary_limit = float(input("\nEnter salary threshold to filter employees: "))
display_employees_above_salary(filename, salary_limit)

