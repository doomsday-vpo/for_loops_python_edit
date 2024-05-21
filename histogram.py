import sys

left_boundary_p1 = 0
right_boundary_p1 = 199
left_boundary_p2 = 200
right_boundary_p2 = 399
left_boundary_p3 = 400
right_boundary_p3 = 599
left_boundary_p4 = 600
right_boundary_p4 = 799
left_boundary_p5 = 800
right_boundary_p5 = 1000

num_count = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for _ in range(num_count):
    cur_number = int(input())
    if left_boundary_p1 <= cur_number <= right_boundary_p1:
        p1_count += 1
    elif left_boundary_p2 <= cur_number <= right_boundary_p2:
        p2_count += 1
    elif left_boundary_p3 <= cur_number <= right_boundary_p3:
        p3_count += 1
    elif left_boundary_p4 <= cur_number <= right_boundary_p4:
        p4_count += 1
    elif left_boundary_p5 <= cur_number <= right_boundary_p5:
        p5_count += 1

print(f'{p1_count / num_count * 100:.2f}%')
print(f'{p2_count / num_count * 100:.2f}%')
print(f'{p3_count / num_count * 100:.2f}%')
print(f'{p4_count / num_count * 100:.2f}%')
print(f'{p5_count / num_count * 100:.2f}%')
