import math

points_win = 2000
points_final = 1200
points_semifinal = 720
value_win = "W"
value_final = "F"
value_semifinal = "SF"

tournaments = int(input())
initial_points = int(input())
points = 0
win_count = 0

for _ in range(tournaments):
    state = input().lower().strip()

    if state == value_win.lower():
        points += points_win
        win_count += 1
    elif state == value_final.lower():
        points += points_final
    elif state == value_semifinal.lower():
        points += points_semifinal

print(f"Final points: {initial_points + points}")
print(f"Average points: {math.floor(points / tournaments)}")
print(f"{(win_count / tournaments) * 100:.2f}%")

