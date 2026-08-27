"""Account creation and balance module."""

def create_account(account_number, holder_name, initial_balance=0.0):
    return {
        "account_number": account_number,
        "holder_name": holder_name,
        "balance": float(initial_balance)
    }

def get_balance(account):
    return account["balance"]

