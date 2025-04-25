count_groups = int(input())
peak1 = 0
peak2 = 0
peak3 = 0
peak4 = 0
peak5 = 0
total_people = 0
for _ in range(count_groups):
    people = int(input())
    if people <=5:
        peak1+=people
        total_people+=people
    elif 6<= people <=12:
        peak2+=people
        total_people += people
    elif 13<= people <=25:
        peak3+=people
        total_people += people
    elif 26<= people<=40:
        peak4 +=people
        total_people += people
    else:
        peak5+=people
        total_people += people

print(f'{peak1/total_people*100:.2f}%')
print(f'{peak2/total_people*100:.2f}%')
print(f'{peak3/total_people*100:.2f}%')
print(f'{peak4/total_people*100:.2f}%')
print(f'{peak5/total_people*100:.2f}%')



