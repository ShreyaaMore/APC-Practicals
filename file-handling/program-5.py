# 5.	Write a program to count and display the total number of lines present in a text file.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        line_count = sum(1 for _ in f)
    print(f"Total number of lines: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

