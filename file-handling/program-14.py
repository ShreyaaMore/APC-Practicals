# 14.	Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.

filename = input("Enter the input file name: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new replacement word: ")
output_filename = input("Enter output file name: ").strip()

if not output_filename:
    output_filename = filename

try:
    with open(filename, "r") as f:
        content = f.read()

    modified_content = content.replace(old_word, new_word)

    with open(output_filename, "w") as f:
        f.write(modified_content)

    print(f"All occurrences of '{old_word}' replaced with '{new_word}'.")
    print(f"Saved successfully to '{output_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

