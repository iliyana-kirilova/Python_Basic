floors = int(input())
flats = int(input())
flat_name = ''

for floor_number in range (floors,0, -1):
    for flat_number in range(flats):
        if floor_number == floors:
            flat_name = f'L{floor_number}{flat_number}'
        elif floor_number%2==0:
            flat_name = f'O{floor_number}{flat_number}'
        else:
            flat_name = f'A{floor_number}{flat_number}'

        print(flat_name, end= ' ')

    print()
