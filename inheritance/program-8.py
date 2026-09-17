# 8.	Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_base_info(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Basic: Rs. {self.basic_salary:.2f}")


class Manager(Employee):
    def calculate_salary(self):
        allowance = 0.45 * self.basic_salary
        return self.basic_salary + allowance

    def display(self):
        self.display_base_info()
        print(f"Role: Manager | Total Salary: Rs. {self.calculate_salary():.2f}\n")


class Developer(Employee):
    def calculate_salary(self):
        allowance = 0.35 * self.basic_salary
        return self.basic_salary + allowance

    def display(self):
        self.display_base_info()
        print(f"Role: Developer | Total Salary: Rs. {self.calculate_salary():.2f}\n")


class Tester(Employee):
    def calculate_salary(self):
        allowance = 0.20 * self.basic_salary
        return self.basic_salary + allowance

    def display(self):
        self.display_base_info()
        print(f"Role: Tester | Total Salary: Rs. {self.calculate_salary():.2f}\n")


m = Manager("M101", "Vikram Malhotra", 70000.0)
d = Developer("D201", "Shreya More", 60000.0)
t = Tester("T301", "Neha Chawla", 50000.0)

print("Employee Salaries Across Roles")
m.display()
d.display()
t.display()
