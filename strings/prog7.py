# Remove all spaces from the input string.

text = input("Enter a string: ")
cleaned_text = ""

for character in text:
    if character != " ":
        cleaned_text += character

print(f"String without spaces: {cleaned_text}")