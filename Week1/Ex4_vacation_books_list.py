import math

count_pages = int(input())
count_pages_per_hour = int(input())
count_days = int(input())

total_hours = count_pages/count_pages_per_hour
hours_per_day = total_hours/count_days
print(math.floor(hours_per_day))
