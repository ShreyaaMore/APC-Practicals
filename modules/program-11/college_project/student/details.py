"""Student details module."""

def get_student_details(roll_no, name, branch, semester):
    return {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "semester": semester
    }

def display_student_info(student):
    print("Student Information:")
    print(f"Roll No  : {student['roll_no']}")
    print(f"Name     : {student['name']}")
    print(f"Branch   : {student['branch']}")
    print(f"Semester : {student['semester']}")

