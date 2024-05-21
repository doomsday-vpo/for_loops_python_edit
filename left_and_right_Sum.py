n = int(input())

left_sum = 0
right_sum = 0

for i in range(n):
    num = int(input())
    left_sum += num

for i in range(n):
    num = int(input())
    right_sum += num

if left_sum == right_sum:
    print("Yes, sum =", left_sum)
else:
    diff = abs(left_sum - right_sum)
    print("No, diff =", diff)
