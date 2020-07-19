# credit_principal = int(input('Enter the credit principal: '))
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'


# print(credit_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

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

