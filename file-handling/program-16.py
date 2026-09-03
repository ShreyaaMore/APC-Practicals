# 16.	Read a text file and create another file containing the same text in uppercase.

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            fout.write(line.upper())

    print(f"File contents converted to uppercase and saved to '{output_file}'.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")

