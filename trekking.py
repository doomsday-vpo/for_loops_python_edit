left_boundary_musala = 1
right_boundary_musala = 5
left_boundary_montblanc = 6
right_boundary_montblanc = 12
left_boundary_kili = 13
right_boundary_kili = 25
left_boundary_k2 = 26
right_boundary_k2 = 40
left_boundary_everest = 41

number_of_groups = int(input())

total_people = 0
people_for_musala = 0
people_for_montblanc = 0
people_for_kili = 0
people_for_k2 = 0
people_for_everest = 0

for _ in range(number_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= right_boundary_musala:
        people_for_musala += number_of_people
    elif left_boundary_montblanc <= number_of_people <= right_boundary_montblanc:
        people_for_montblanc += number_of_people
    elif left_boundary_kili <= number_of_people <= right_boundary_kili:
        people_for_kili += number_of_people
    elif left_boundary_k2 <= number_of_people <= right_boundary_k2:
        people_for_k2 += number_of_people
    elif number_of_people >= left_boundary_everest:
        people_for_everest += number_of_people

print(f"{(people_for_musala / total_people) * 100:.2f}%")
print(f"{(people_for_montblanc / total_people) * 100:.2f}%")
print(f"{(people_for_kili / total_people) * 100:.2f}%")
print(f"{(people_for_k2 / total_people) * 100:.2f}%")
print(f"{(people_for_everest / total_people) * 100:.2f}%")



