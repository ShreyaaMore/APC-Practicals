def calculate_slab_amount(units):
    if units <= 100:
        return units * 2.0
    elif units <= 200:
        return 100 * 2.0 + (units - 100) * 3.0
    elif units <= 300:
        return 100 * 2.0 + 100 * 3.0 + (units - 200) * 4.5
    else:
        return 100 * 2.0 + 100 * 3.0 + 100 * 4.5 + (units - 300) * 6.0

def calculate_fixed_charges():
    return 50.0

def calculate_tax(amount, tax_rate=18):
    return (amount * tax_rate) / 100

def calculate_discount(amount, discount_rate=5):
    return (amount * discount_rate) / 100

def generate_total_bill(units):
    energy_charges = calculate_slab_amount(units)
    fixed_charges = calculate_fixed_charges()
    subtotal = energy_charges + fixed_charges
    tax = calculate_tax(subtotal, 18)
    discount = calculate_discount(subtotal, 5)
    total = subtotal + tax - discount
    return energy_charges, fixed_charges, tax, discount, total

units = 250
energy, fixed, tax, discount, total = generate_total_bill(units)
print("Energy Charges: Rs.", energy)
print("Fixed Charges: Rs.", fixed)
print("Tax (18%): Rs.", tax)
print("Discount (5%): Rs.", discount)
print("Total Bill: Rs.", total)
