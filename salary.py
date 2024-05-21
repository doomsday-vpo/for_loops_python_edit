tabs = int(input())
salary = int(input())
fine_amount = 0

site_facebook = "Facebook"
fine_facebook = 150
site_instagram = "Instagram"
fine_instagram = 100
site_reddit = "Reddit"
fine_reddit = 50

for i in range(tabs):
    site_name = input().lower().strip()

    if site_name == site_facebook.lower():
        fine_amount += fine_facebook
    elif site_name == site_instagram.lower():
        fine_amount += fine_instagram
    elif site_name == site_reddit.lower():
        fine_amount += fine_reddit
    if fine_amount >= salary:
        break


if fine_amount >= salary:
    print("You have lost your salary.")

else:
    print(int(salary - fine_amount))


