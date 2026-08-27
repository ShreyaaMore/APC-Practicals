# Define a function that accepts a string and returns the number of vowels present in it

def vowels(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count+=1

    return count

s = input("Enter a string: ")

print("Number of Vowels:", vowels(s))