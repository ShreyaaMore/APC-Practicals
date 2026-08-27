"""Student module containing functions for result evaluation."""

def calculate_total(marks_list):
    return sum(marks_list)

def calculate_percentage(marks_list, max_marks_per_subject=100):
    total_max = len(marks_list) * max_marks_per_subject
    if total_max == 0:
        return 0.0
    return (calculate_total(marks_list) / total_max) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"

