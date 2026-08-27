def deposit(account, amount):
    account["balance"] += amount
    account["transactions"].append(f"Deposited: Rs.{amount}")
    print(f"Successfully deposited Rs.{amount}")

def withdraw(account, amount):
    if amount > account["balance"]:
        print("Insufficient balance!")
    else:
        account["balance"] -= amount
        account["transactions"].append(f"Withdrew: Rs.{amount}")
        print(f"Successfully withdrew Rs.{amount}")

def balance_enquiry(account):
    print(f"Current Balance: Rs.{account['balance']}")
    return account["balance"]

def transaction_history(account):
    print("Transaction History:")
    for tx in account["transactions"]:
        print(tx)

account = {"balance": 1000, "transactions": []}
deposit(account, 500)
withdraw(account, 200)
withdraw(account, 2000)
balance_enquiry(account)
transaction_history(account)
