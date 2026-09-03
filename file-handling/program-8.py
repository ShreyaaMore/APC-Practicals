# 8.	Write a program to read a text file and display its lines in reverse order.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        lines = f.readlines()
        print("\nLines in reverse order:")
        for line in reversed(lines):
            print(line.rstrip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

