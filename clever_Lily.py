bday_money_increase = 10
little_brother = 1

age = int(input())
washing_machine = float(input())
toy_price = float(input())

money_for_bday = 0
money_saved = 0
toys_count = 0

for bday in range(1, age + 1):
    if bday % 2 == 0:
        money_for_bday += bday_money_increase
        money_saved += money_for_bday - little_brother

    else:
        toys_count += 1

money_from_toys = toys_count * toy_price
total_money_saved = money_saved + money_from_toys

if total_money_saved >= washing_machine:
    print(f'Yes! {total_money_saved - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_money_saved:.2f}')
