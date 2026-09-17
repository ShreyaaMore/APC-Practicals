# 13.	Create a base class Person with a method display_role(). Derive Student, Faculty, and Administrator. Override the method to display the respective role. Store all objects in a list and invoke the same method using a loop.

class Person:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        print(f"{self.name} has an unspecified role in the institution.")


class Student(Person):
    def display_role(self):
        print(f"[Student] {self.name}: Attends lectures, works on assignments, and takes exams.")


class Faculty(Person):
    def display_role(self):
        print(f"[Faculty] Prof. {self.name}: Delivers academic lectures, grades exams, and leads research.")


class Administrator(Person):
    def display_role(self):
        print(f"[Administrator] {self.name}: Manages college registrations, campus facilities, and finances.")


people = [
    Student("Aarav Mehta"),
    Faculty("S. R. Kulkarni"),
    Administrator("Nitin Jadhav"),
    Student("Diya Sharma")
]

print("Institutional Directory (Polymorphic Roles)")
for person in people:
    person.display_role()
