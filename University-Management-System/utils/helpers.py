from university_system.config import GPA_SCALE

def format_currency(amount):
    return f"₹{amount:,.0f}"


def gpa_label(gpa):
    if gpa >= 9.0:
        return "Outstanding"
    elif gpa >= 7.5:
        return "Excellent"
    elif gpa >= 6.0:
        return "Good"
    elif gpa >= 5.0:
        return "Average"
    else:
        return "Below Average"


def percentage_to_gpa(percentage):
    return round((percentage / 100.0) * GPA_SCALE, 2)
