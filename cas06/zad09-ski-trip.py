'''
9. Ski Trip
John decided to spend his vacation in a ski resort. Before he leaves, however, he must book a hotel and calculate how much his stay will cost. The following types of accommodation are available, with the following accommodation prices:
            ▪ "room for one person" – 18.00 USD per night
            ▪ "apartment" – 25.00 USD per night
            ▪ "president apartment" – 35.00 USD per night
Depending on the number of days he will stay in the hotel (example: 11 days = 10 nights) and the type of room he chooses, he can enjoy different discounts.
The discounts are as follows:
'''
days = int(input())
room_type = input()
grade = input()

discount = 0.00
price = 0.00

days -= 1

if (room_type == "room for one person"):
    price = 18.00
    # discount = 0
elif(room_type == "apartment"):
    price = 25.00
    if (days < 10):
        discount = 0.3
    elif (10 <= days <= 15):
        discount = 0.35
    elif (days > 15):
        discount = 0.5
elif room_type == "president apartment":
    price = 35.00
    if (days < 10):
        discount = (10 / 100)
    elif (10 <= days <= 15):
        discount = (15 / 100)
    elif (days > 15):
        discount = (20/100)

total_price = days * price

# sad racunamo discount
# nova cena ce da bude (1.00 - popust) * cena

# total_price = (1.00 - discount) * total_price
total_price = total_price - discount * total_price

if(grade == 'positive'):
    # imamo 100 posto cene i dodamo jos 25% to je 125% od cene
    total_price = (125/100) * total_price
elif(grade == 'negative'):
    # imamo 100 posto cene i oduzmemo 10 posto, to je 90% od cene
    total_price = (90/100) * total_price
print(f'{total_price:.2f}')