# 6.	Create a base class Student with a method calculate_grade(). Derive EngineeringStudent, MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.

class Student:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def calculate_grade(self):
        return "Pass"


class EngineeringStudent(Student):
    def calculate_grade(self):
        if self.percentage >= 85:
            return "Distinction (A+)"
        elif self.percentage >= 75:
            return "First Class (A)"
        elif self.percentage >= 60:
            return "Second Class (B)"
        elif self.percentage >= 45:
            return "Pass Class (C)"
        else:
            return "Fail (F)"


class MedicalStudent(Student):
    def calculate_grade(self):
        if self.percentage >= 90:
            return "Honors (A+)"
        elif self.percentage >= 80:
            return "Excellent (A)"
        elif self.percentage >= 70:
            return "Good (B)"
        elif self.percentage >= 60:
            return "Satisfactory (C)"
        else:
            return "Unsatisfactory (F)"


class ManagementStudent(Student):
    def calculate_grade(self):
        if self.percentage >= 80:
            return "Executive Honors (A)"
        elif self.percentage >= 65:
            return "Merit (B)"
        elif self.percentage >= 50:
            return "Pass (C)"
        else:
            return "Fail (F)"


students = [
    EngineeringStudent("Kavita", 78),
    MedicalStudent("Rishi", 78),
    ManagementStudent("Tanya", 78)
]

print("Discipline-Specific Grading (Same 78% Score)")
for s in students:
    print(f"Domain: {s.__class__.__name__:<20} | Student: {s.name:<8} | Grade: {s.calculate_grade()}")
