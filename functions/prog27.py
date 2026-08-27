def consultation_charges(specialist_fee):
    return specialist_fee

def laboratory_charges(tests):
    return sum(tests)

def medicine_charges(medicines):
    return sum(medicines)

def room_charges(days, rate_per_day):
    return days * rate_per_day

def calculate_discount(total, category):
    if category.lower() == "senior":
        return total * 0.20
    elif category.lower() == "child":
        return total * 0.10
    elif category.lower() == "staff":
        return total * 0.30
    return 0.0

def generate_hospital_bill(consultation, tests, medicines, days, room_rate, category):
    c_fee = consultation_charges(consultation)
    l_fee = laboratory_charges(tests)
    m_fee = medicine_charges(medicines)
    r_fee = room_charges(days, room_rate)
    gross_total = c_fee + l_fee + m_fee + r_fee
    discount = calculate_discount(gross_total, category)
    final_bill = gross_total - discount
    return gross_total, discount, final_bill

gross, disc, net = generate_hospital_bill(500, [300, 700], [250, 450], 3, 1000, "senior")
print("Gross Total: Rs.", gross)
print("Discount: Rs.", disc)
print("Final Hospital Bill: Rs.", net)
