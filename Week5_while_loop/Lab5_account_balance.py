available_sum = 0

while True:
    data = input()

    if data =='NoMoreMoney':
        break

    current_money = float(data)

    if current_money>=0:
        available_sum +=current_money
        print(f'Increase: {current_money:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {available_sum:.2f}')
