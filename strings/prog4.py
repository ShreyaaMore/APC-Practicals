# Check whether the entered string is a palindrome. 

s = input("Enter a string: ").lower()

reversed_string = ""

for char in s:
    reversed_string = char + reversed_string

if s == reversed_string:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")