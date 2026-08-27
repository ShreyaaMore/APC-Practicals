def calculate_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100
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
    return percentage, grade

m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))

percentage, grade = calculate_grade(m1, m2, m3, m4, m5)
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
