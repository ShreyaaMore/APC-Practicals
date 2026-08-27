def add_product(cart, name, price, qty):
    cart.append({"name": name, "price": price, "qty": qty})

def remove_product(cart, name):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            break

def calculate_subtotal(cart):
    return sum(item["price"] * item["qty"] for item in cart)

def apply_coupon(subtotal, coupon_code):
    if coupon_code == "SAVE10":
        return subtotal * 0.10
    elif coupon_code == "SAVE20":
        return subtotal * 0.20
    return 0.0

def calculate_gst(amount, gst_rate=18):
    return (amount * gst_rate) / 100

def generate_invoice(cart, coupon_code=""):
    subtotal = calculate_subtotal(cart)
    discount = apply_coupon(subtotal, coupon_code)
    discounted_amount = subtotal - discount
    gst = calculate_gst(discounted_amount, 18)
    total = discounted_amount + gst
    print("--- INVOICE ---")
    for item in cart:
        print(f"{item['name']} - {item['qty']} x Rs.{item['price']} = Rs.{item['qty']*item['price']}")
    print("Subtotal: Rs.", subtotal)
    print("Discount: Rs.", discount)
    print("GST (18%): Rs.", gst)
    print("Final Total: Rs.", total)

cart = []
add_product(cart, "Shirt", 800, 2)
add_product(cart, "Jeans", 1500, 1)
add_product(cart, "Cap", 300, 1)
remove_product(cart, "Cap")
generate_invoice(cart, "SAVE10")
