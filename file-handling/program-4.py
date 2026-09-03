# 4.	Write a program to read a text file line by line and display each line separately.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        print("\nDisplaying file line by line:")
        for line_no, line in enumerate(f, start=1):
            print(f"Line {line_no}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

