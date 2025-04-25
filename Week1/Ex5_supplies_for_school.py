pen = int(input())
markers = int(input())
board_detergent = int(input())
discount = int(input())

price_pen = pen*5.80
price_markers = markers*7.20
price_detergent = board_detergent*1.20
sum = price_pen + price_markers + price_detergent
discount_sum = sum - (sum*discount/100)

print(discount_sum)
