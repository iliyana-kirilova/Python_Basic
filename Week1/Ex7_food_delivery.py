count_chicken = int(input())
count_fish = int(input())
count_vegetarian = int(input())

price_chicken = count_chicken*10.35
price_fish = count_fish*12.40
price_vegetarian = count_vegetarian*8.15
price = price_chicken+price_fish+price_vegetarian

total_price = price + (price*0.20) + 2.5
print(total_price)