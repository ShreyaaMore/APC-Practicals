# 15.	Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def get_student_info(self):
        return f"{self.get_person_info()}, Roll No: {self.roll_no}, Course: {self.course}"


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_full_profile(self):
        print("Multilevel Inheritance: Research Scholar Profile")
        print(self.get_student_info())
        print(f"Research Topic : {self.research_topic}")
        print(f"Guide Name     : {self.guide_name}\n")


scholar = ResearchStudent("Rohan Deshmukh", 27, "RS-2024", "Computer Science", "Quantum Machine Learning", "Dr. A. Verma")
scholar.display_full_profile()
