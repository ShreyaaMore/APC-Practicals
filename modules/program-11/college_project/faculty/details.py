"""Faculty details module."""

def get_faculty_details(faculty_id, name, department, designation):
    return {
        "faculty_id": faculty_id,
        "name": name,
        "department": department,
        "designation": designation
    }

def display_faculty_info(faculty):
    print("Faculty Information")
    print(f"Faculty ID  : {faculty['faculty_id']}")
    print(f"Name        : {faculty['name']}")
    print(f"Department  : {faculty['department']}")
    print(f"Designation : {faculty['designation']}")

