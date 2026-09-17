# 6.	Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = float(balance)

    def display_account(self):
        print(f"Account Number : {self.account_no}")
        print(f"Balance        : Rs. {self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    def display_savings(self):
        self.display_account()
        print(f"Interest Rate  : {self.interest_rate}%")
        print(f"Annual Interest: Rs. {self.calculate_interest():.2f}")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, bonus_cashback, complimentary_lounge_access):
        super().__init__(account_no, balance, interest_rate)
        self.bonus_cashback = bonus_cashback
        self.complimentary_lounge_access = complimentary_lounge_access

    def display_premium_details(self):
        print("Premium Savings Account Details")
        self.display_savings()
        print(f"Cashback Benefit: {self.bonus_cashback}% on all debit transactions")
        print(f"Airport Lounge  : {'Yes' if self.complimentary_lounge_access else 'No'}\n")


psa = PremiumSavingsAccount("SB-908123", 250000.0, 4.5, 2.0, True)
psa.display_premium_details()
