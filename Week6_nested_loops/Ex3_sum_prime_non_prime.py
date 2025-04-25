command = input()
number_is_prime = 0
non_prime = 0

while command != 'stop':
    number = int(command)

    if number<0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for divisor in range(2,number):
        if number%divisor==0:
            is_prime = False
            break

    if is_prime:
        number_is_prime+=number
    else:
        non_prime +=number


    command = input()
print(f'Sum of all prime numbers is: {number_is_prime}')
print(f'Sum of all non prime numbers is: {non_prime}')