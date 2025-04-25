nylon = int(input())
paint = int(input())
thinner = int(input())
hours_of_work = int(input())

price_nylon = (nylon +2) *1.50
price_paint = (paint*1.1)*14.50
price_thinner = thinner*5
supplies_sum = price_nylon + price_paint + price_thinner +0.40
work_price = (supplies_sum*0.30)*hours_of_work
total_price = supplies_sum+work_price
print(total_price)
