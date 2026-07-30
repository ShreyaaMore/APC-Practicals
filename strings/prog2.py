# Count the number of vowels, consonants, digits, spaces, and special characters in a given string

s = input("Enter a string: ").lower()

vowels = 0
consonants = 0
sp_ch = 0
digits = 0
spaces = 0

for i in s:
    if i in "aeiou":
        vowels += 1
    elif i in "qwrtypsdfghjklzxcvbnm":
        consonants+= 1
    elif i == " ":
        spaces += 1
    elif i in "0123456789":
        digits += 1
    else:
        sp_ch+=1


print(f"No. of vowels: {vowels} \n No. of consonants: {consonants} \n No. of digits: {digits}\n No. of spaces: {spaces}\n No. of special characters: {sp_ch}")