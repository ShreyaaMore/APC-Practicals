# 13.	Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"StudentResult object created for {self.name}.")

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total() / (len(self.marks) * 100)) * 100

    def calculate_grade(self):
        pct = self.calculate_percentage()
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 50:
            return "D"
        else:
            return "F (Fail)"

    def display_report(self):
        print(f"\nResult for {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Total      : {self.calculate_total()} / {len(self.marks) * 100}")
        print(f"Percentage : {self.calculate_percentage():.2f}%")
        print(f"Grade      : {self.calculate_grade()}\n")

    def __del__(self):
        print(f"Destructor: StudentResult record for {self.name} is cleared from memory.")


sr = StudentResult("Shreya More", [88, 92, 85, 90, 94])
sr.display_report()
del sr
