# Validate whether a given email address follows a valid format.

email = input("Enter an email address: ")

if email.count("@") == 1 and "." in email and " " not in email:
    
    print("Valid email address!")
else:
    print("Invalid email address!")