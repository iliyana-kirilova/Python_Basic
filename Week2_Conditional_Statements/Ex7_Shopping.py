budget = float(input())
videocards = int(input())
processors = int(input())
ram_memory= int(input())

price_videocards = videocards*250
price_processors = processors*(price_videocards*0.35)
price_ram_memory = ram_memory*(price_videocards*0.10)

total_price = price_videocards+price_processors+price_ram_memory
if videocards>processors:
    total_price*=0.85

diff= abs(budget-total_price)
if budget<total_price:
    print(f'Not enough money! You need {diff:.2f} leva more!')
else:
    print(f'You have {diff:.2f} leva left!')
