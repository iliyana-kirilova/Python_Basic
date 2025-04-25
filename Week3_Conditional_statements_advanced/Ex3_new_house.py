flowers = input()
count_flowers = int(input())
budget = int(input())
price = 0
if flowers == "Roses":
    if count_flowers>80:
        price = (count_flowers*5)*0.90
    else:
        price = count_flowers*5
elif flowers == "Dahlias":
    if count_flowers>90:
        price = (count_flowers*3.80)*0.85
    else:
        price = count_flowers*3.80
elif flowers == "Tulips":
   if count_flowers>80:
       price = (count_flowers * 2.80) * 0.85
   else:
       price = count_flowers*2.80
elif flowers == "Narcissus":
    if count_flowers<120:
        price = (count_flowers * 3) * 1.15
    else:
        price = count_flowers*3
elif flowers == "Gladiolus":
    if count_flowers<80:
        price = (count_flowers * 2.5) * 1.20
    else:
        price = count_flowers*2.5

diff = abs(budget-price)
if budget>=price:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")