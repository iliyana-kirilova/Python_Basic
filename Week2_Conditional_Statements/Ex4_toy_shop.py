trip_price = float(input())
puzzles = int(input())
doll = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_price = puzzles*2.60 + doll*3 + bears* 4.1 + minions*8.20 + trucks*2
count_toys = puzzles+doll+bears+minions+trucks
if count_toys>=50:
    total_price*=0.75

total_price*=0.90
diff = abs(total_price-trip_price)
if trip_price<=total_price:
    print(f'Yes! {diff:.2f} lv left.')
else: print(f'Not enough money! {diff:.2f} lv needed.')