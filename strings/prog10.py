# Display each character of a string along with its ASCII value.

s = input("Enter a string: ")

print("Character -> ASCII Value")
for char in s:
    print(f"'{char}' -> {ord(char)}")