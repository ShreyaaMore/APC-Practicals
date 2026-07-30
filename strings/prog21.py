# Validate a password based on these conditions:
# - Minimum 8 characters
# - At least one uppercase letter
# - One lowercase letter
# - One digit
# - One special character

password = input("Enter a password: ")

min_len = len(password) >= 8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(not char.isalnum() for char in password)

if min_len and upper and lower and digit and special:
    print("Password is Valid.")
else:
    print("Password is Invalid. Requirements:")

    if not min_len:
        print("- Minimum 8 characters")

    if not upper:
        print("- At least one uppercase letter")

    if not lower:
        print("- At least one lowercase letter")

    if not digit:
        print("- At least one digit")
        
    if not special:
        print("- At least one special character")