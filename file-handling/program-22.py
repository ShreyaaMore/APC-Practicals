# 22.	Read the contents of two text files and create a third file containing the contents of both files.

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
output_file = input("Enter the output file name to store combined contents: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    with open(output_file, "w") as out:
        out.write(content1)
        if content1 and not content1.endswith("\n"):
            out.write("\n")
        out.write(content2)

    print(f"Contents of '{file1}' and '{file2}' successfully merged into '{output_file}'.")
except FileNotFoundError as e:
    print(f"Error: {e}")

