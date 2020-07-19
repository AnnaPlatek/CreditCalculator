import math
input_value = int(input())
area = 2 * math.sqrt(3) * pow(input_value, 2)
volume = 1 / 3 * math.sqrt(2) * pow(input_value, 3)
print(round(area, 2), round(volume, 2))