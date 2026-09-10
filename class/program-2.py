# 2.	Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.basic_salary

    def calculate_da(self):
        return 0.10 * self.basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display_details(self):
        print(f"Employee ID  : {self.emp_id}")
        print(f"Name         : {self.name}")
        print(f"Basic Salary : Rs. {self.basic_salary:.2f}")
        print(f"HRA (20%)    : Rs. {self.calculate_hra():.2f}")
        print(f"DA (10%)     : Rs. {self.calculate_da():.2f}")
        print(f"Gross Salary : Rs. {self.calculate_gross_salary():.2f}\n")


emp = Employee("EMP101", "Rajesh Deshmukh", 50000.0)
emp.display_details()
