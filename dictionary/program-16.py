# 16.	Create two dictionaries and merge them into a single dictionary.


students_A = {
    101: "Mikhil",
    102: "Shreya",
    103: "Ravi",
    104: "Jignesh",
    105: "Tom"
}

students_B = {
    106: "Mia",
    107: "Goli",
    108: "Pappu",
    109: "Raju",
    110: "Ramesh"
}

print("Dictionary A:", students_A)
print("Dictionary B:", students_B)

students = students_A
for id, name in students_B.items():
    students[id] = name

print("Combined Dict:", students)