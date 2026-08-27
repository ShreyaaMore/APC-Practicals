"""Customer shipping address module."""

addresses = {}

def add_address(cid, street, city, pincode):
    addresses[cid] = {
        "street": street,
        "city": city,
        "pincode": pincode
    }
    return addresses[cid]

def get_address(cid):
    return addresses.get(cid)

