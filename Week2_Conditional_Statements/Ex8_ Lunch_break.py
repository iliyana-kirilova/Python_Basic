from math import ceil
name = str(input())
duration_episod = int(input())
duration_break = int(input())

time_lunch = duration_break/8
time_to_rest = duration_break/4

rest_time = duration_break - time_lunch-time_to_rest

diff = abs(rest_time-duration_episod)
if rest_time>=duration_episod:
    print(f'You have enough time to watch {name} and left with {ceil(diff)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name}, you need {ceil(diff)} more minutes.')