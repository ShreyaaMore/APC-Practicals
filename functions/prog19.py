def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4.0
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 100 * 4.0 + (units - 300) * 5.0
    return bill

units = float(input("Enter units consumed: "))
print("Electricity Bill: Rs.", calculate_electricity_bill(units))
