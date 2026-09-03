# 20.	Store deposits and withdrawals in a file. Read the file and calculate: 
# •	Total deposits 
# •	Total withdrawals 
# •	Final balance 
# •	Largest transaction

import os

filename = "transactions.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Type,Amount\n")
        f.write("Deposit,15000\n")
        f.write("Withdrawal,3000\n")
        f.write("Deposit,5000\n")
        f.write("Withdrawal,8500\n")
        f.write("Deposit,12000\n")
        f.write("Withdrawal,2000\n")
    print(f"Sample transactions written to '{filename}'.")

total_deposits = 0.0
total_withdrawals = 0.0
transactions = []

with open(filename, "r") as f:
    f.readline()
    for line in f:
        line = line.strip()
        if line:
            tx_type, amount_str = line.split(",")
            amount = float(amount_str)
            transactions.append((tx_type.strip(), amount))

            if tx_type.strip().lower() == "deposit":
                total_deposits += amount
            elif tx_type.strip().lower() == "withdrawal":
                total_withdrawals += amount

final_balance = total_deposits - total_withdrawals

print("\nTransaction Summary")
print(f"Total Deposits   : {total_deposits:.2f}")
print(f"Total Withdrawals: {total_withdrawals:.2f}")
print(f"Final Balance    : {final_balance:.2f}")

if transactions:
    largest_tx = max(transactions, key=lambda t: t[1])
    print(f"Largest Transaction: {largest_tx[0]} of {largest_tx[1]:.2f}")
else:
    print("No transactions found.")

