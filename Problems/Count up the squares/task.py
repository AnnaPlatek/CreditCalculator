# put your python code here
my_sum = 0
sq_sum = 0
while True:
    number = int(input())
    my_sum += number
    sq_sum += (number * number)
    if my_sum == 0:
        break
print(sq_sum)
