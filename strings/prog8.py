# Find the number of times a specified character appears in a string.

s = input("Enter a string: ")
target = input("Enter a character to search: ")

count = 0
for char in s:
    if char == target:
        count += 1

print(f"Character '{target}' appears {count} times.")