# Store student details in a tuple:
# •	Roll Number 
# •	Name 
# •	Department 
# •	Marks 

student_details = (
    (106, "Shreya", "CSE", 98), 
    (105, "Mikhil", "CSE", 95), 
    (20, "Siddhi", "DS", 92), 
    (19, "Vaishnavi", "AIML", 93)
                   )
print("Student details: ")

for student in student_details:
    print(student)