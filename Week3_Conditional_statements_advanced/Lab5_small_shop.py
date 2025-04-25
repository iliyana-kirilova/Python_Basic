
product = input()
town= input()
quantity = float(input())
price= 0
if product == 'coffee':
    if town == 'Sofia':
        price = 0.5
    elif town == 'Plovdiv':
        price = 0.4
    elif town == 'Varna':
        price = 0.45
if product == 'water':
    if town == 'Sofia':
        price = 0.8
    elif town == 'Plovdiv':
        price = 0.7
    elif town == 'Varna':
        price = 0.7
if product == 'beer':
    if town == 'Sofia':
        price = 1.2
    elif town == 'Plovdiv':
        price = 1.15
    elif town == 'Varna':
        price = 1.10
if product == 'sweets':
    if town == 'Sofia':
        price = 1.45
    elif town == 'Plovdiv':
        price = 1.30
    elif town == 'Varna':
        price = 1.35
if product == 'peanuts':
    if town == 'Sofia':
        price = 1.60
    elif town == 'Plovdiv':
        price = 1.50
    elif town == 'Varna':
        price = 1.55

final_price = price*quantity
print(final_price)