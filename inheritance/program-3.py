# 3.	Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.

class Academic:
    def __init__(self, academic_marks):
        self.academic_marks = academic_marks

    def display_academic(self):
        print(f"Academic Marks : {self.academic_marks} / 100")


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

    def display_sports(self):
        print(f"Sports Points  : {self.sports_points} / 50")


class Student(Academic, Sports):
    def __init__(self, name, roll_no, academic_marks, sports_points):
        Academic.__init__(self, academic_marks)
        Sports.__init__(self, sports_points)
        self.name = name
        self.roll_no = roll_no

    def calculate_overall_performance(self):
        academic_pct = (self.academic_marks / 100) * 100
        sports_pct = (self.sports_points / 50) * 100
        overall = (academic_pct * 0.70) + (sports_pct * 0.30)
        return overall

    def display_profile(self):
        print(f"Roll No             : {self.roll_no}")
        print(f"Name                : {self.name}")
        self.display_academic()
        self.display_sports()
        print(f"Overall Performance : {self.calculate_overall_performance():.2f}%\n")


s = Student("Shreya More", 106, 92, 44)
print("Overall Student Performance")
s.display_profile()
