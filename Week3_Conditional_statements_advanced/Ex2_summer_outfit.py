degree = int(input())
day_time = input()
outfit = ''
shoes = ''
match day_time:
    case 'Morning':
       if 10<=degree<=18:
            outfit = 'Sweatshirt'
            shoes = 'Sneakers'
       elif 18< degree<=24:
           outfit = 'Shirt'
           shoes = 'Moccasins'
       else:
           outfit = 'T-Shirt'
           shoes = 'Sandals'
    case 'Afternoon':
        if 10 <= degree <= 18:
            outfit = 'Shirt'
            shoes = 'Moccasins'
        elif 18 < degree <= 24:
            outfit = 'T-Shirt'
            shoes = 'Sandals'
        else:
            outfit = 'Swim Suit'
            shoes = 'Barefoot'
    case 'Evening':
        if 10 <= degree <= 18:
            outfit = 'Shirt'
            shoes = 'Moccasins'
        elif 18 < degree <= 24:
            outfit = 'Shirt'
            shoes = 'Moccasins'
        else:
            outfit = 'Shirt'
            shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")