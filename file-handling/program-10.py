# 10.	Read a text file and calculate the number of alphabets, digits, spaces, and special characters.

filename = input("Enter the file name: ")

alphabets = 0
digits = 0
spaces = 0
special_chars = 0

try:
    with open(filename, "r") as f:
        text = f.read()
        for char in text:
            if char.isalpha():
                alphabets += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                special_chars += 1

    print(f"Alphabets: {alphabets}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")
    print(f"Special Characters: {special_chars}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

