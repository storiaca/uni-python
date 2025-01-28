'''
4. Fishing Boat
Tony and his friends loved to go fishing. They were so passionate about fishing that they decided to go fishing by boat. The price of renting a boat depends on the season and the number of fishermen.
The price depends on the season: 
    • The price for renting a boat in the spring is 3000 USD
    • The price for renting a boat in summer and autumn is 4200 USD.
    • The price for renting a boat in winter is 2600 USD.
Depending on the number of people, the group receives a discount:
    • If the group is up to 6 people inclusive – a 10% discount.
    • If the group is from 7 to 11 people inclusive - a 15% discount
    • If the group is more than 12 people - a 25% discount 
'''
group_budget = int(input())
season = input()
num_fishermen = int(input())

price = 0.00

if(season == "Spring"):
    price = 3000
elif (season == "Summer"):
    price = 4200
elif (season == "Autumn"):
    price = 4200
elif (season == "Winter"):
    price = 2600

if(num_fishermen <= 6):
    # 10% popusta na cenu: 100 - 10 = 90
    price = (90 / 100) * price
elif  (7 < num_fishermen <= 11):
    # 15% popusta: 100 - 15 = 85
    price = (85 / 100) * price
elif (num_fishermen > 12):
    # 25% popusta: 100 - 25 = 75
    price = (75 / 100) * price

if((num_fishermen % 2 == 0) and (season != 'Autumn')):
    price = (95 / 100) * price

if (group_budget >= price):
    print(f"Yes! You have {(group_budget - price):.2f} USD left.")
else:
    print(f"Not enough money! You need {(price - group_budget):.2f} USD.")