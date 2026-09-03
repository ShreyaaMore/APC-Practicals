# 7.	Write a program to count the total number of characters in a text file, including spaces.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(f"Total number of characters (including spaces): {len(content)}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

