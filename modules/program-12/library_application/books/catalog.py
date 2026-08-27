"""Book catalog module."""

books_db = {}

def add_book(book_id, title, author):
    books_db[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }
    return books_db[book_id]

def find_book(book_id):
    return books_db.get(book_id)

def list_books():
    return books_db

