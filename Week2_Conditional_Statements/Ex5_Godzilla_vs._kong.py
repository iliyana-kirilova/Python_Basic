budget = float(input())
extra = int (input())
clothing = float(input())
price_clothing = 0
decor = budget*0.10
if extra>150:
    price_clothing = clothing*extra*0.90
else:
    price_clothing = clothing*extra

total_price = decor +price_clothing
diff = abs(budget-total_price)
if budget>=total_price:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')