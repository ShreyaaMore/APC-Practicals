"""Module for calculating total and percentage marks."""

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks, max_marks_per_subject=100):
    total_possible = len(marks) * max_marks_per_subject
    if total_possible == 0:
        return 0.0
    return (sum(marks) / total_possible) * 100

