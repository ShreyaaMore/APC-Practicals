def calculate_gross_salary(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    gross = basic + hra + da
    return gross

basic = float(input("Enter basic salary: "))
print("Gross Salary:", calculate_gross_salary(basic))
