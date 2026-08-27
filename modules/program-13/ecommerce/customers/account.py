"""Customer account module."""

customers = {}

def create_customer(cid, name, email):
    customers[cid] = {"name": name, "email": email}
    return customers[cid]

def get_customer(cid):
    return customers.get(cid)

