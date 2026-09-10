# 9.	Design an ATM class that allows a user to:
# a)	Check balance 
# b)	Deposit money 
# c)	Withdraw money 
# d)	Display account details
# Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_no, holder_name, balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = float(balance)

    def check_balance(self):
        print(f"Current Balance: Rs. {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")
            self.check_balance()

    def display_details(self):
        print(f"Account Number : {self.account_no}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : Rs. {self.balance:.2f}")


def menu():
    atm = ATM("1234567890", "Shreya More", 15000.0)

    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amt = float(input("Enter amount to deposit: "))
            atm.deposit(amt)
        elif choice == "3":
            amt = float(input("Enter amount to withdraw: "))
            atm.withdraw(amt)
        elif choice == "4":
            atm.display_details()
        elif choice == "5":
            print("Thank you for using our ATM service. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    menu()
