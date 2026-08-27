"""Module for attendance eligibility."""

def calculate_attendance_percentage(attended, total):
    if total == 0:
        return 0.0
    return (attended / total) * 100

def check_eligibility(attended, total, threshold=75.0):
    pct = calculate_attendance_percentage(attended, total)
    return pct >= threshold

