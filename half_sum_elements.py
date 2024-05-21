import sys

num_count = int(input())
num_sum = 0
max_number = -sys.maxsize

for _ in range(num_count):
    cur_num = int(input())
    num_sum += cur_num
    if cur_num > max_number:
        max_number = cur_num

if num_sum / 2 == max_number:
    print("Yes")
    print("Sum =", max_number)
else:
    print("No")
    print("Diff =", abs(max_number - (num_sum - max_number)))
