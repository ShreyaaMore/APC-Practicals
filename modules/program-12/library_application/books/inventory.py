"""Book inventory module."""
from books.catalog import books_db

def is_available(book_id):
    book = books_db.get(book_id)
    return book is not None and book["available"]

def set_availability(book_id, status):
    if book_id in books_db:
        books_db[book_id]["available"] = status
        return True
    return False

