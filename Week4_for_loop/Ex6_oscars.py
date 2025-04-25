actor_name = input()
academy_points= float(input())
count_evaluator = int(input())

total_points = academy_points
for _ in range(count_evaluator):
    name_of_evaluator = input()
    points_evaluator = float(input())

    total_points+= len(name_of_evaluator)*points_evaluator/2

    if total_points>1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
