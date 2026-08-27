# 9.	Create a dictionary of programming languages and their creators. Display each key and value using a loop.

languages_creator = {
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich",
    "PHP": "Rasmus Lerdorf",
    "Python": "Guido van Rossum"
}

print("Programming language and their creators:")

for language in languages_creator:
    print(f"{language} was created by {languages_creator[language]}")