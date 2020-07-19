import math
angle_in_deg = int(input())
angle_in_rad = math.radians(angle_in_deg)
cotangent = 1 / math.tan(angle_in_rad)
print(round(cotangent, 10))