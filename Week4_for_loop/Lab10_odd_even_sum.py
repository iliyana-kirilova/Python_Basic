n = int(input())
odd_sum =0
even_sum =0
for position in range (n):
    num = int(input())
    if position%2!=0:
        odd_sum +=num
    else:
        even_sum+=num

if odd_sum==even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum-even_sum)
    print('No')
    print(f'Diff = {diff}')
