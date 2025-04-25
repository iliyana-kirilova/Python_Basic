mackerel_price = float(input()) #скумрия
sprat_price = float(input()) #цаца
bonito = float(input()) #паламуд
scad = float(input()) #сафрид
mussel = float(input()) #миди

price_bonito_per_kilo = mackerel_price*1.6
total_price_bonito = bonito * price_bonito_per_kilo

price_scad_per_kilo = sprat_price*1.8
total_price_scad = scad * price_scad_per_kilo

price_mussel = mussel*7.5
total_price = total_price_bonito + total_price_scad + price_mussel
print('%.2f'%total_price)