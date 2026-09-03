# 6.	Write a program to count the total number of words present in a text file.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        text = f.read()
        words = text.split()
        print(f"Total number of words: {len(words)}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

