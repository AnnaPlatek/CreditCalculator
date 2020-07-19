import math
first_number = int(input())
second_number = int(input())

if second_number < 0 or second_number == 0 or second_number == 1:
    value = math.log(first_number, math.e)
else:
    value = math.log(first_number, second_number)
print(round(value, 2))