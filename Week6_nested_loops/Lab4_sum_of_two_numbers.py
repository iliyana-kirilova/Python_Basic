start = int(input())
end = int(input())
magic_number = int(input())
combination_counter = 0
flag = False

for x in range (start, end +1):
    for y in range (start, end +1):
        combination_counter += 1
        if x+y ==magic_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            flag = True
            break
    if flag:
       break

else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")


