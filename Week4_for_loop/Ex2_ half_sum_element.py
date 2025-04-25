number = int(input())
max_number =0
total_sum = 0

for _ in range(number):
    current_num = int(input())

    if current_num>max_number:
        max_number=current_num

    total_sum+=current_num

total_sum-=max_number

if total_sum==max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(total_sum-max_number)
    print("No")
    print(f"Diff = {diff}")