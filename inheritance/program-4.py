# 4.	Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal(self):
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age} years")


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

    def display_professional(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Designation : {self.designation}")
        print(f"Salary      : Rs. {self.salary:.2f}")


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display_employee_info(self):
        print("Complete Employee Profile")
        self.display_personal()
        self.display_professional()
        print()


emp = Employee("Sunita Rao", 29, "EMP452", "Lead Software Engineer", 95000.0)
emp.display_employee_info()
