# Create a list of books.
# Implement:
# •	Add a new book 
# •	Search a book 
# •	Remove a book 
# •	Display all books 
# •	Count total books

books = []
choice = ""

while(choice<='5'):

    print("1. Add a new book \n2. Search a  book\n3. Remove a book \n4. Display all books\n5. Count total books\n")
    choice = input("Enter a choice: ")

    if choice == '1':
        item = input("Enter a book: ")
        books.append(item)

    elif choice == '2':
            item = input("Enter a book to search: ")
            if item in books:
                position = books.index(item) + 1
                print("Book found at position:", position)
            else:
                print("Book not found.")

    elif choice == '3':
        if len(books)>0:
            item = input("Enter a book to be removed: ")
            books.remove(item)

    elif choice == '4':
        print(f"The list of books is: {books}")

    elif choice == '5':
        length = len(books)
        print("Total number of books is",length)

    else:
        print("Invalid Input")