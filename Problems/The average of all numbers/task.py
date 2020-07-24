# put your python code here
a = int(input())
b = int(input())
sum = 0
divisor = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum = sum + i
        divisor = divisor + 1
print(sum / divisor)

