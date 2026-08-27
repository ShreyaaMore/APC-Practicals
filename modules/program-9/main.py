# 9.	Develop a package banking containing:
# a)	account.py – account creation and balance 
# b)	transaction.py – deposit and withdrawal 
# c)	loan.py – loan calculation 
# Create a main program to use the package.

from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_emi, calculate_total_payment

acc = create_account("AC1001", "Shreya More", 10000.0)
print(f"Account Created for {acc['holder_name']} (A/C: {acc['account_number']})")
print(f"Current Balance: Rs. {get_balance(acc):.2f}")

deposit(acc, 5000.0)
print(f"After Depositing Rs. 5000: Rs. {get_balance(acc):.2f}")

withdraw(acc, 3200.0)
print(f"After Withdrawing Rs. 3200: Rs. {get_balance(acc):.2f}")

loan_amount = 200000.0
rate = 8.5  
tenure = 3 
emi = calculate_emi(loan_amount, rate, tenure)
total_pay = calculate_total_payment(loan_amount, rate, tenure)

print(f"\nLoan Calculation:")
print(f"Loan Amount        : Rs. {loan_amount:.2f}")
print(f"Annual Interest    : {rate}%")
print(f"Tenure             : {tenure} years")
print(f"Monthly EMI        : Rs. {emi:.2f}")
print(f"Total Amount Payable: Rs. {total_pay:.2f}")

