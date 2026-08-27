"""Student marks module."""

def get_student_marks(marks_dict):
    total = sum(marks_dict.values())
    percentage = (total / (len(marks_dict) * 100)) * 100
    return {
        "subjects": marks_dict,
        "total": total,
        "percentage": percentage
    }

def display_student_marks(marks_info):
    print("Marks Breakdown:")
    for subject, score in marks_info["subjects"].items():
        print(f" - {subject}: {score}")
    print(f"Total Marks: {marks_info['total']}")
    print(f"Percentage : {marks_info['percentage']:.2f}%")

