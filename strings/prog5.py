# Count the number of uppercase and lowercase letters in a string. 

s = input("Enter a string: ")

uppercase = 0
lowercase = 0

for i in s:
    if i.isupper():
        uppercase += 1

    elif i.islower():
        lowercase += 1

print(f"No. of Uppercase letters: {uppercase}\nNo. of Lowercase letters: {lowercase}")
    