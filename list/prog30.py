# 	Store patient names and ages using lists.
#     Perform:
# •	Add a patient 
# •	Delete a patient 
# •	Search a patient 
# •	Display all patients 
# •	Count total patients

patients_list = []
choice = ""

while(choice<='5'):

    print("1. Add a patient \n2. Delete a patient\n3. Search a patient \n4. Display all patients\n5. Count total patients\n")

    choice = input("Enter a choice: ")

    if choice == '1':
        item = input("Enter a patient: ")
        patients_list.append(item)

    elif choice == '2':
        if len(patients_list)>0:
            item = input("Enter a patient name to be removed: ")
            patients_list.remove(item)

    elif choice == '3':
        item = input("Enter a patient to search: ")
        if item in patients_list:
            position = patients_list.index(item) + 1
            print("Patient found at position:", position)
        else:
            print("Patient not found.")

    elif choice == '4':
        print(f"The Patients List is: {patients_list}")

    elif choice == '5':
        length = len(patients_list)
        print("The total number of patients is",length)

    else:
        print("Invalid Input")