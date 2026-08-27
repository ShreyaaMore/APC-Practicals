"""Order processing module."""

orders = {}

def place_order(order_id, customer_id, cart, final_amount):
    orders[order_id] = {
        "customer_id": customer_id,
        "items": cart,
        "total": final_amount,
        "status": "Confirmed"
    }
    return orders[order_id]

