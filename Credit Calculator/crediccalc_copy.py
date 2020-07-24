# part 1
credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)

# part 2

import math

credit_principal = int(input('Enter the credit principal: '))
thing_to_calculate = input("""What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment: """)
if thing_to_calculate == "m":
    monthly_payment = int(input('Enter monthly payment: '))
    count_of_months = round(credit_principal / monthly_payment)
    print('It takes {0} month to repay the credit'.format(count_of_months))
elif thing_to_calculate == "p":
    count_of_months = int(input('Enter count of months: '))
    monthly_payment = math.ceil(credit_principal / count_of_months)
    last_payment = credit_principal - (count_of_months - 1) * monthly_payment
    print(monthly_payment)
    print('Your monthly payment = {0} with last month payment = {1}.'.format(monthly_payment, last_payment))

#part 3
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