"""Billing and receipt module."""

def generate_invoice(order_id, customer, items, subtotal, tax, total):
    print("\n============== INVOICE ==============")
    print(f"Order ID : {order_id}")
    print(f"Customer : {customer['name']} ({customer['email']})")
    print("-" * 37)
    for it in items:
        p = it["product"]
        q = it["quantity"]
        print(f"{p['name']} x{q}: Rs. {p['price'] * q:.2f}")
    print("-" * 37)
    print(f"Subtotal : Rs. {subtotal:.2f}")
    print(f"Tax (18%): Rs. {tax:.2f}")
    print(f"Total    : Rs. {total:.2f}")
    print("=====================================")

