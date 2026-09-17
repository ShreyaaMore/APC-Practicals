# 3.	Create an abstract class BankAccount with abstract methods deposit() and withdraw(). Derive SavingsAccount and CurrentAccount and implement the required operations.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, acc_no, balance=0.0):
        self.acc_no = acc_no
        self.balance = float(balance)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance=0.0, min_balance=1000.0):
        super().__init__(acc_no, balance)
        self.min_balance = min_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"[Savings {self.acc_no}] Deposited: Rs. {amount:.2f} | Balance: Rs. {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < self.min_balance:
            print(f"[Savings {self.acc_no}] Withdrawal rejected: Minimum balance of Rs. {self.min_balance:.2f} must be maintained.")
        else:
            self.balance -= amount
            print(f"[Savings {self.acc_no}] Withdrawn: Rs. {amount:.2f} | Balance: Rs. {self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, balance=0.0, overdraft_limit=20000.0):
        super().__init__(acc_no, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"[Current {self.acc_no}] Deposited: Rs. {amount:.2f} | Balance: Rs. {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < -self.overdraft_limit:
            print(f"[Current {self.acc_no}] Withdrawal rejected: Exceeds overdraft limit of Rs. {self.overdraft_limit:.2f}.")
        else:
            self.balance -= amount
            print(f"[Current {self.acc_no}] Withdrawn: Rs. {amount:.2f} | Balance: Rs. {self.balance:.2f}")


sa = SavingsAccount("SB-1001", 5000.0)
ca = CurrentAccount("CA-2002", 10000.0)

print("Savings Account")
sa.deposit(2000.0)
sa.withdraw(5500.0)
sa.withdraw(1000.0)

print("\nCurrent Account")
ca.withdraw(25000.0)
