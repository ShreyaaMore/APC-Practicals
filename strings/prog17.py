# Check whether two strings are anagrams

word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")