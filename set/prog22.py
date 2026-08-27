emp1_skills = {"Python", "SQL", "Git", "Docker", "Machine Learning"}
emp2_skills = {"Java", "SQL", "Kubernetes", "Docker", "AWS"}
common_skills = emp1_skills & emp2_skills
unique_emp1 = emp1_skills - emp2_skills
unique_emp2 = emp2_skills - emp1_skills
all_skills = emp1_skills | emp2_skills

print("Employee 1 Skills:", emp1_skills)
print("Employee 2 Skills:", emp2_skills)
print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_emp1)
print("Skills unique to Employee 2:", unique_emp2)
print("All available skills:", all_skills)
