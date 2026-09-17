# 12.	Develop an online shopping payment module using polymorphism. Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement its own make_payment() method. Demonstrate polymorphism using a common function.

class Payment:
    def __init__(self, amount):
        self.amount = float(amount)

    def make_payment(self):
        print(f"Processing generic payment of Rs. {self.amount:.2f}")


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def make_payment(self):
        print(f"[UPI] Requesting Rs. {self.amount:.2f} from Virtual Payment Address: {self.upi_id}...")
        print("      Transaction verified with UPI PIN. Payment SUCCESSFUL.")


class CardPayment(Payment):
    def __init__(self, amount, card_number_last4, card_type="Credit"):
        super().__init__(amount)
        self.card_number_last4 = card_number_last4
        self.card_type = card_type

    def make_payment(self):
        print(f"[CARD] Authorizing Rs. {self.amount:.2f} on {self.card_type} card ending in {self.card_number_last4}...")
        print("       3D-Secure OTP verified. Payment SUCCESSFUL.")


class WalletPayment(Payment):
    def __init__(self, amount, wallet_name, mobile_no):
        super().__init__(amount)
        self.wallet_name = wallet_name
        self.mobile_no = mobile_no

    def make_payment(self):
        print(f"[WALLET] Deducting Rs. {self.amount:.2f} from {self.wallet_name} linked to {self.mobile_no}...")
        print("         Wallet balance updated. Payment SUCCESSFUL.")


def checkout(payment_method):
    print("\nCheckout Gate")
    payment_method.make_payment()


payments = [
    UPIPayment(1499.0, "shreya@okaxis"),
    CardPayment(8500.0, "4312", "Credit"),
    WalletPayment(350.0, "Paytm Wallet", "+91-9876543210")
]

for p in payments:
    checkout(p)
