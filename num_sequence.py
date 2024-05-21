import sys

n = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for number in range(n):
    new_number = int(input())
    if new_number > max_number:
        max_number = new_number
    if new_number < min_number:
        min_number = new_number


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
