price_vegetables = float(input())
price_fruit = float(input())
vegetable_weight = int(input())
fruit_weight = int(input())
sum = price_vegetables * vegetable_weight + price_fruit * fruit_weight
sum_euro = sum / 1.94
print(f'{sum_euro:.2f}')
