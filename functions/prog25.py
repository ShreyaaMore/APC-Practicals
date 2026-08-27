def add_book(library, book_id, title, copies):
    if book_id in library:
        library[book_id]["copies"] += copies
    else:
        library[book_id] = {"title": title, "copies": copies}
    print(f"Book '{title}' added successfully.")

def issue_book(library, book_id):
    if book_id in library and library[book_id]["copies"] > 0:
        library[book_id]["copies"] -= 1
        print(f"Book '{library[book_id]['title']}' issued successfully.")
    elif book_id in library:
        print("Book is currently out of stock.")
    else:
        print("Book not found.")

def return_book(library, book_id):
    if book_id in library:
        library[book_id]["copies"] += 1
        print(f"Book '{library[book_id]['title']}' returned successfully.")
    else:
        print("Book does not belong to this library.")

def search_book(library, title):
    for book_id, info in library.items():
        if info["title"].lower() == title.lower():
            print(f"Found: ID={book_id}, Title={info['title']}, Available Copies={info['copies']}")
            return
    print("Book not found.")

def display_books(library):
    print("Available Books:")
    for book_id, info in library.items():
        print(f"ID: {book_id}, Title: {info['title']}, Copies: {info['copies']}")

library = {}
add_book(library, 101, "Python Programming", 3)
add_book(library, 102, "Data Structures", 2)
display_books(library)
issue_book(library, 101)
search_book(library, "Python Programming")
return_book(library, 101)
display_books(library)
