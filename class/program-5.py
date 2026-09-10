# 5.	Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Price   : Rs. {self.price:.2f}\n")


b1 = Book("B101", "Python Crash Course", "Eric Matthes", 850.0)
b2 = Book("B102", "Clean Code", "Robert C. Martin", 1200.0)
b3 = Book("B103", "The Pragmatic Programmer", "Andrew Hunt", 1450.0)

print("Book Information")
b1.display()
b2.display()
b3.display()
