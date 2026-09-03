# 15.	Read a Python source file and create another file after removing single-line comments.

input_file = input("Enter the Python source file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            stripped = line.strip()
            
            if stripped.startswith("#"):
                continue
            
            if "#" in line:
                code_part = line.split("#", 1)[0].rstrip()
                fout.write(code_part + "\n")
            else:
                fout.write(line)

    print(f"Single-line comments removed successfully. Saved to '{output_file}'.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")

