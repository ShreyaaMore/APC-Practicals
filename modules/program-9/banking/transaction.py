"""Deposit and withdrawal module."""

def deposit(account, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > account["balance"]:
        raise ValueError("Insufficient balance.")
    account["balance"] -= amount
    return account["balance"]

