# 13.	Create a directory named ecommerce containing packages for:
# a)	Products 
# b)	Customers 
# c)	Orders 
# d)	Payments 
# Each package should contain at least two modules.

from products.catalog import get_product, list_products
from products.pricing import calculate_discounted_price, calculate_tax
from customers.account import create_customer, get_customer
from customers.address import add_address, get_address
from orders.cart import create_cart, add_to_cart, get_cart_total
from orders.order_process import place_order
from payments.gateway import process_payment
from payments.billing import generate_invoice

print("E-Commerce Store Simulation\n")

customer = create_customer("C01", "Shreya More", "mikhil@example.com")
address = add_address("C01", "123 Academic Way", "Pune", "411001")
print(f"Customer Logged In: {customer['name']}, Address: {address['city']}")

print("\nAvailable Products:")
for pid, info in list_products().items():
    print(f" - [{pid}] {info['name']}: Rs. {info['price']}")

cart = create_cart()
add_to_cart(cart, get_product("P101"), 1)
add_to_cart(cart, get_product("P102"), 2)

subtotal = get_cart_total(cart)
tax = calculate_tax(subtotal, 18.0)
final_total = subtotal + tax

order = place_order("ORD-5001", "C01", cart, final_total)
print(f"\nOrder Created: {order['status']} with {len(cart)} items.")

pay_result = process_payment(final_total, method="Credit Card")
print(f"Payment Status: {pay_result['status']} (Transaction ID: {pay_result['tx_id']})")

generate_invoice("ORD-5001", customer, cart, subtotal, tax, final_total)

