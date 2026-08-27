"""Module salary_utils containing salary computation functions."""

def calculate_gross_salary(basic_pay, hra, da, allowances=0.0):
    return basic_pay + hra + da + allowances

def calculate_deductions(pf, tax, other_deductions=0.0):
    return pf + tax + other_deductions

def calculate_net_salary(gross_salary, total_deductions):
    return gross_salary - total_deductions

