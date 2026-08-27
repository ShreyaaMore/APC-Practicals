def calculate_bill(prices, quantities, discount_percent=10):
    total = 0
    for p, q in zip(prices, quantities):
        total += p * q
    discount = (total * discount_percent) / 100
    final_bill = total - discount
    return final_bill

prices = [100, 250, 50]
quantities = [2, 1, 4]
print("Total Bill after discount:", calculate_bill(prices, quantities, 10))
