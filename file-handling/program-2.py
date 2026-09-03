# 2.	Write a program to open a text file and display its complete contents.

filename = input("Enter the file name to open: ")

try:
    with open(filename, "r") as f:
        contents = f.read()
        print("\nFile Contents:")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

