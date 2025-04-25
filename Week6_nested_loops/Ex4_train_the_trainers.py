judges_count = int(input())
total_sum =0
total_judge_score= 0

command = input()
while command !='Finish':
    current_presentation = command
    current_score = 0
    for _ in range (judges_count):
        judges_score = float(input())
        current_score+=judges_score

    average_score = current_score/judges_count
    print(f'{current_presentation} - {average_score:.2f}.')

    total_sum +=current_score
    total_judge_score += judges_count
    command = input()

total_average = total_sum/total_judge_score
print(f'Student\'s final assessment is {total_average:.2f}.')