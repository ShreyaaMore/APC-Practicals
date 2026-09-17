# 1.	Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee ID    : {self.emp_id}")
        print(f"Name           : {self.name}")
        print(f"Monthly Salary : Rs. {self.salary:.2f}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def calculate_annual_salary(self):
        return self.salary * 12

    def display_manager_details(self):
        self.display_employee_details()
        print(f"Department     : {self.department}")
        print(f"Annual Salary  : Rs. {self.calculate_annual_salary():.2f}\n")


m = Manager("MGR201", "Pooja Hegde", 85000.0, "Engineering")
print("Manager Details")
m.display_manager_details()
