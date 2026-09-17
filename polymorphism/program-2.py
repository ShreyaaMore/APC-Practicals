# 2.	Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and Tester classes. Override the method in each class to calculate salary according to the employee's role.

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def calculate_salary(self):
        return self.base_pay


class Manager(Employee):
    def __init__(self, name, base_pay, incentive):
        super().__init__(name, base_pay)
        self.incentive = incentive

    def calculate_salary(self):
        return self.base_pay + self.incentive + (0.20 * self.base_pay)


class Developer(Employee):
    def __init__(self, name, base_pay, overtime_hours, hourly_rate=500):
        super().__init__(name, base_pay)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.base_pay + (self.overtime_hours * self.hourly_rate)


class Tester(Employee):
    def __init__(self, name, base_pay, bugs_caught, bonus_per_bug=200):
        super().__init__(name, base_pay)
        self.bugs_caught = bugs_caught
        self.bonus_per_bug = bonus_per_bug

    def calculate_salary(self):
        return self.base_pay + (self.bugs_caught * self.bonus_per_bug)


employees = [
    Manager("Rajesh", 80000, 20000),
    Developer("Shreya", 65000, 25),
    Tester("Pooja", 45000, 30)
]

print("Polymorphic Salary Calculation")
for emp in employees:
    print(f"Role: {emp.__class__.__name__:<10} | Name: {emp.name:<8} | Total Salary: Rs. {emp.calculate_salary():.2f}")
