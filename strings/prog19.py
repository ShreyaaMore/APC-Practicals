# Check whether a given substring exists in the main string.

s1 = input("Enter the main string: ")
s2 = input("Enter the substring to search: ")

if s2 in s1:
    print(f"Substring '{s2}' exists in the main string.")
else:
    print(f"Substring '{s2}' does not exist in the main string.")