# 28. Create a dictionary containing names and phone numbers.
# Implement: • Add contact 
# • Search contact 
# • Update contact 
# • Delete contact 
# • Display all contacts

contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210"
}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added contact {name}.")

def search_contact(name):
    if name in contacts:
        print(f"Contact: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Updated contact {name}.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact {name}.")
    else:
        print(f"Contact {name} not found.")

def display_all_contacts():
    print("All contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


display_all_contacts()
add_contact("Charlie", "555-123-4567")
search_contact("Bob")
update_contact("Alice", "111-222-3333")
delete_contact("Bob")
display_all_contacts()
