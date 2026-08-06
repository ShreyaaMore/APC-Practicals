# Create a list of student names. Remove:
# •	First student 
# •	Last student 
# •	A specific student by name 

names = ["Shreya", "Aaradhya", "Aadya", "Ruhi", "Mikhil"]

print("Original list: ", names)
names.remove(names[0])
names.remove(names[-1])
names.remove("Aaradhya")

print("Updated list: ",names)