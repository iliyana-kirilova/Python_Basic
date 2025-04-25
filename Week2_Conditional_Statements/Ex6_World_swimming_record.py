import math

record_in_second = float(input())
distance = float(input())
time_per_meter = float(input())

time_swimming = distance*time_per_meter
delay = math.floor(distance/15)*12.5
total_time = time_swimming+delay
if total_time<record_in_second:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    diff = abs(record_in_second-total_time)
    print(f'No, he failed! He was {diff:.2f} seconds slower.')