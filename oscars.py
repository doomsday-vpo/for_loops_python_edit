max_points = 1250.50

actor_name = input()
academy_points = float(input())
juror_count = int(input())

actor_total_points = academy_points

for i in range(juror_count):
    juror_name = input()
    juror_points = float(input())
    juror_final_points = (len(juror_name) * juror_points) / 2
    actor_total_points += juror_final_points

    if actor_total_points > max_points:
        break

if actor_total_points > max_points:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(max_points - actor_total_points):.1f} more!")

