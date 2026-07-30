marital_status = input("Enter your marital status: ").lower()
gender = input("Enter your gender: ").lower()
age = int(input("Enter your age: "))

if marital_status=="married":
    print("You are insured")

elif marital_status=="unmarried":
    if gender=="male" and age>30:
        print("You are insured")
    elif gender=="female" and age>25:
        print("You are insured")
    else:
        print("You are not insured")

else:
    print("Your are not insured")