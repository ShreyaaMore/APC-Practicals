# 29. Create a dictionary containing book IDs and book names.
# Implement: • Add a book 
# • Search a book 
# • Remove a book 
# • Display all books 
# • Count total books

books = {
    101: "Python Programming", 
    102: "Data Structures"
}

def add_book(book_id, name):
    books[book_id] = name
    print(f"Added book '{name}' with ID {book_id}.")

def search_book(book_id):
    if book_id in books:
        print(f"Book ID: {book_id}, Name: {books[book_id]}")
    else:
        print(f"Book ID {book_id} not found.")

def remove_book(book_id):
    if book_id in books:
        name = books.pop(book_id)
        print(f"Removed book '{name}' (ID {book_id}).")
    else:
        print(f"Book ID {book_id} not found.")

def display_all_books():
    print("All books:")
    for book_id, name in books.items():
        print(f"ID: {book_id}, Name: {name}")

def count_total_books():
    print(f"Total books: {len(books)}")


display_all_books()
add_book(103, "Algorithms")
search_book(102)
remove_book(101)
display_all_books()
count_total_books()
