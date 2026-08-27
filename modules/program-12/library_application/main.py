# 12.	Create a directory structure for a library application with separate packages for:
# a)	Books 
# b)	Members 
# c)	Transactions 
# Each package should contain suitable modules and a main program should combine all functionality.

from books.catalog import add_book, list_books
from members.registration import register_member, list_members
from transactions.borrow import issue_book, return_book, transaction_history

print("Library Application Management:\n")

add_book("B01", "Fluent Python", "Luciano Ramalho")
add_book("B02", "Clean Architecture", "Robert Martin")
add_book("B03", "Designing Data-Intensive Applications", "Martin Kleppmann")

print("Books Catalog:")
for b_id, info in list_books().items():
    status = "Available" if info["available"] else "Issued"
    print(f"[{b_id}] {info['title']} by {info['author']} ({status})")

register_member("M01", "Shreya More", "mikhil@example.com")
register_member("M02", "Aarav Sharma", "aarav@example.com")

print("\nRegistered Members:")
for m_id, info in list_members().items():
    print(f"[{m_id}] {info['name']} ({info['email']})")

print("\nPerforming Transactions:")
success, msg = issue_book("B01", "M01")
print(f"Issue B01 to M01: {msg}")

success, msg = issue_book("B01", "M02")
print(f"Issue B01 to M02: {msg}")

success, msg = return_book("B01", "M01")
print(f"Return B01 from M01: {msg}")

print("\nTransaction Log:")
for tx in transaction_history:
    print(f"Action: {tx['action']} | Book: {tx['book_id']} | Member: {tx['member_id']}")

