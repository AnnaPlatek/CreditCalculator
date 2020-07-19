import math
x = int(input())
logistic_function = (math.exp(x)) / (math.exp(x) + 1)
print(round(logistic_function, 2))