# Create a tuple containing patient records:
# •	Patient ID 
# •	Name 
# •	Age 
# •	Blood Group 
# Perform the following operations:
# •	Display all records 
# •	Search for a patient by ID 
# •	Count the total number of patients 
# •	Display patients with a specific blood group 

patient_record = (
    (112, "Shyam", 32, "B+ve"),
    (134, "Neha", 44, "B+ve"),
    (185, "Riya", 28, "O+ve"),
    (104, "Siya", 36, "B-ve"),
    (121, "Nidhi", 29, "A-ve"),
)

print("Patient records: ")

for patient in patient_record:
    print(patient)

n = int(input("Enter an ID to search: "))

found = False

for patient in patient_record:
    if patient[0]==n:
        found = True
        print(patient[1])

if found == False:
    print("Patient not found")


print("\nThe total number of patients is ", len(patient_record))

blood_group = input("\nEnter blood group to search: ")

print("Patients with blood group", blood_group, ":")
for patient in patient_record:
    if patient[3] == blood_group:
        print(patient)
