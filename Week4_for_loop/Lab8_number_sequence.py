import sys
smallest_number = sys.maxsize
biggest_number = -sys.maxsize

n= int(input())
for _ in range (n):
    number = int(input())
    if number<smallest_number:
        smallest_number = number
    if number>biggest_number:
        biggest_number = number

print(f"Max number: {biggest_number}")
print(f"Min number: {smallest_number}")