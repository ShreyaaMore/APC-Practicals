# 21.	Maintain book records containing book ID, title, author, and availability status. Implement operations to: 
# •	Add a book. 
# •	Search for a book. 
# •	Issue a book. 
# •	Return a book. 
# •	Display available books.

import os

filename = "books.txt"

def initialize_file():
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("BookID,Title,Author,Status\n")
            f.write("B101,Python Programming,John Zelle,Available\n")
            f.write("B102,Clean Code,Robert Martin,Available\n")
            f.write("B103,Introduction to Algorithms,CLRS,Issued\n")
            f.write("B104,Operating System Concepts,Silberschatz,Available\n")

def read_all_books():
    books = []
    if not os.path.exists(filename):
        return books
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            line = line.strip()
            if line:
                b_id, title, author, status = line.split(",")
                books.append({
                    "id": b_id.strip(),
                    "title": title.strip(),
                    "author": author.strip(),
                    "status": status.strip()
                })
    return books

def save_all_books(books):
    with open(filename, "w") as f:
        f.write("BookID,Title,Author,Status\n")
        for b in books:
            f.write(f"{b['id']},{b['title']},{b['author']},{b['status']}\n")

def add_book():
    b_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    
    books = read_all_books()
    for b in books:
        if b["id"].lower() == b_id.lower():
            print(f"Error: Book with ID '{b_id}' already exists.")
            return

    books.append({"id": b_id, "title": title, "author": author, "status": "Available"})
    save_all_books(books)
    print("Book added successfully.")

def search_book():
    query = input("Enter Book ID or Title to search: ").strip().lower()
    books = read_all_books()
    found = False
    for b in books:
        if query == b["id"].lower() or query in b["title"].lower():
            print(f"Found: [ID: {b['id']}] Title: {b['title']}, Author: {b['author']}, Status: {b['status']}")
            found = True
    if not found:
        print("Book not found.")

def issue_book():
    b_id = input("Enter Book ID to issue: ").strip().lower()
    books = read_all_books()
    for b in books:
        if b["id"].lower() == b_id:
            if b["status"].lower() == "available":
                b["status"] = "Issued"
                save_all_books(books)
                print(f"Book '{b['title']}' has been issued successfully.")
            else:
                print(f"Book '{b['title']}' is already issued.")
            return
    print("Book not found.")

def return_book():
    b_id = input("Enter Book ID to return: ").strip().lower()
    books = read_all_books()
    for b in books:
        if b["id"].lower() == b_id:
            if b["status"].lower() == "issued":
                b["status"] = "Available"
                save_all_books(books)
                print(f"Book '{b['title']}' has been returned successfully.")
            else:
                print(f"Book '{b['title']}' was not issued.")
            return
    print("Book not found.")

def display_available_books():
    books = read_all_books()
    available = [b for b in books if b["status"].lower() == "available"]
    print("\nAvailable Books:")
    if not available:
        print("No books currently available.")
        return
    print(f"{'Book ID':<10} {'Title':<30} {'Author':<20}")
    print()
    for b in available:
        print(f"{b['id']:<10} {b['title']:<30} {b['author']:<20}")

def menu():
    initialize_file()
    while True:
        print("\n=== Library Book Management ===")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Display Available Books")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_available_books()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    menu()

