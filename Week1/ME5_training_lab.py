import math

w = float(input())*100
h = float(input())*100
p_w = math.floor(w / 120)
p_h = math.floor((h - 100) / 70)
n = p_w * p_h - 3
print(n)