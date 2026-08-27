"""Loan calculation module."""

def calculate_emi(principal, annual_interest_rate, tenure_years):
    r = (annual_interest_rate / 12) / 100
    n = tenure_years * 12
    if r == 0:
        return principal / n
    emi = (principal * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
    return emi

def calculate_total_payment(principal, annual_interest_rate, tenure_years):
    emi = calculate_emi(principal, annual_interest_rate, tenure_years)
    n = tenure_years * 12
    return emi * n

