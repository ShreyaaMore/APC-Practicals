"""Borrow and return transactions module."""
from books.catalog import find_book
from books.inventory import is_available, set_availability
from members.registration import get_member

transaction_history = []

def issue_book(book_id, member_id):
    book = find_book(book_id)
    member = get_member(member_id)

    if not book:
        return False, "Book not found."
    if not member:
        return False, "Member not found."
    if not is_available(book_id):
        return False, f"Book '{book['title']}' is currently not available."

    set_availability(book_id, False)
    member["borrowed_books"].append(book_id)
    transaction_history.append({"action": "ISSUE", "book_id": book_id, "member_id": member_id})
    return True, f"Book '{book['title']}' issued to {member['name']}."

def return_book(book_id, member_id):
    book = find_book(book_id)
    member = get_member(member_id)

    if not book or not member:
        return False, "Book or member not found."
    if book_id not in member["borrowed_books"]:
        return False, "This member did not borrow this book."

    set_availability(book_id, True)
    member["borrowed_books"].remove(book_id)
    transaction_history.append({"action": "RETURN", "book_id": book_id, "member_id": member_id})
    return True, f"Book '{book['title']}' returned by {member['name']}."

