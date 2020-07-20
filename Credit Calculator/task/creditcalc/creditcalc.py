import math

to_calculate = input("""What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal: 
""")

if to_calculate == "n":
    credit_principal = int(input("Enter credit principal: "))
    monthly_payment = float(input("Enter monthly payment: "))
    credit_interest = float(input("Enter credit interest: "))
    i = (credit_interest / 100) / 12
    n = math.ceil(math.log(monthly_payment / (monthly_payment - i * credit_principal), 1 + i))
    if n < 12:
        n_str = str(n) + " months"
    elif n == 12:
        n_str = "1 year"
    elif n > 12 and n % 12 == 0:
        n_str = str(n // 12) + " years"
    else:
        n_str = str(n // 12) + " years and " + str(n % 12) + " months"

    print(f'You need {n_str} to repay this credit!')

elif to_calculate == "a":
    credit_principal = int(input("Enter credit principal: "))
    n = int(input("Enter count of periods: "))
    credit_interest = float(input("Enter credit interest: "))
    i = (credit_interest / 100) / 12

    monthly_payment = math.ceil(credit_principal * (i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    print(f'Your annuity payment = {monthly_payment}!')

elif to_calculate == "p":
    monthly_payment = float(input("Enter monthly payment: "))
    n = int(input("Enter count of periods: "))
    credit_interest = float(input("Enter credit interest: "))
    i = (credit_interest / 100) / 12

    credit_principal = math.ceil(monthly_payment / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
    print(f'Your credit principal = {credit_principal}!')