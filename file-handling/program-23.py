# 23.	Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.

from itertools import zip_longest

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        identical = True
        for line_no, (line1, line2) in enumerate(zip_longest(f1, f2, fillvalue=None), start=1):
            if line1 != line2:
                identical = False
                print(f"\nFiles differ at line {line_no}:")
                print(f"'{file1}': {repr(line1)}")
                print(f"'{file2}': {repr(line2)}")
                break

        if identical:
            print(f"\nThe files '{file1}' and '{file2}' are identical.")
except FileNotFoundError as e:
    print(f"Error: {e}")

