# 6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.

employees = {
    1001: "Ramesh",
    1002: "Ravi",
    1003: "Rajesh",
    1004: "Shresh",
    1005: "Jignesh"
}


print("Employees:", employees)

employee = int(input("Enter employee id to check: "))

if employee in employees:
    print(f"Employee {employee} with id {employees[employee]} exists.")
else:
    print("No such Employee.")