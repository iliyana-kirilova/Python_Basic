import math

figure_type = str(input())
area = ''
if figure_type =='square':
    side = float(input())
    area = side*side
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a*side_b
elif figure_type == 'circle':
    radius = float(input())
    area = math.pi*radius**2
elif figure_type == 'triangle':
    base = float(input())
    h = float(input())
    area = base*h/2

print(f"{area:.3f}")