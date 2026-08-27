"""Member registration module."""

members_db = {}

def register_member(member_id, name, email):
    members_db[member_id] = {
        "name": name,
        "email": email,
        "borrowed_books": []
    }
    return members_db[member_id]

def get_member(member_id):
    return members_db.get(member_id)

def list_members():
    return members_db

