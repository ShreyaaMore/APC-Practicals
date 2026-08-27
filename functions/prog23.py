def calculate_student_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade

def calculate_class_average(students):
    total_marks = sum(sum(s["marks"]) for s in students)
    total_subjects = sum(len(s["marks"]) for s in students)
    return total_marks / total_subjects

def find_highest_scorer(students):
    highest = max(students, key=lambda s: sum(s["marks"]))
    return highest["name"], sum(highest["marks"])

def find_lowest_scorer(students):
    lowest = min(students, key=lambda s: sum(s["marks"]))
    return lowest["name"], sum(lowest["marks"])

students = [
    {"name": "Alice", "roll_no": 101, "marks": [85, 90, 78, 92, 88]},
    {"name": "Bob", "roll_no": 102, "marks": [70, 65, 80, 75, 72]},
    {"name": "Charlie", "roll_no": 103, "marks": [95, 98, 92, 96, 94]}
]

for s in students:
    total, percentage, grade = calculate_student_result(s["marks"])
    print(f"Name: {s['name']}, Roll No: {s['roll_no']}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")

print("Class Average:", calculate_class_average(students))
high_name, high_score = find_highest_scorer(students)
print(f"Highest Scorer: {high_name} with {high_score} marks")
low_name, low_score = find_lowest_scorer(students)
print(f"Lowest Scorer: {low_name} with {low_score} marks")
