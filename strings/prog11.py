# Count the total number of words in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

count = 0
for i in words:
    count+=1
print(count)