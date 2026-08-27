available_books = {"Python Basics", "Data Structures", "Algorithms", "Operating Systems", "Computer Networks"}
requested_books = {"Data Structures", "Web Development", "Python Basics", "Machine Learning"}
available_requested = requested_books.intersection(available_books)
unavailable_requested = requested_books - available_books

print("Available Books:", available_books)
print("Requested Books:", requested_books)
print("Requested books that are available:", available_requested)
print("Requested books that are unavailable:", unavailable_requested)
