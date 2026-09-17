# 7.	Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount, CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently for each account type.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = float(balance)

    def calculate_interest(self):
        return 0.0


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.035


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0.0


class FixedDepositAccount(BankAccount):
    def __init__(self, account_no, balance, tenure_years=1):
        super().__init__(account_no, balance)
        self.tenure_years = tenure_years

    def calculate_interest(self):
        return self.balance * 0.0725 * self.tenure_years


accounts = [
    SavingsAccount("SA-101", 100000.0),
    CurrentAccount("CA-202", 100000.0),
    FixedDepositAccount("FD-303", 100000.0, tenure_years=2)
]

print("Interest Comparison for Rs. 100,000 Balance")
for acc in accounts:
    interest = acc.calculate_interest()
    print(f"Account: {acc.__class__.__name__:<20} | Number: {acc.account_no} | Interest Earned: Rs. {interest:.2f}")
