# Reverse the order of words in a sentence without changing the words themselves.

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)
print(f"The reversed sentence is: {result}")