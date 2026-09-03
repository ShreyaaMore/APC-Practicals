# 9.	Read a text file and count the number of vowels and consonants present in the file.

filename = input("Enter the file name: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

try:
    with open(filename, "r") as f:
        text = f.read()
        for char in text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

