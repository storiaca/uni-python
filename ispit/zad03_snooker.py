'''
Snooker Championship
As the World Snooker Championship approaches at the Crucible Theater in Sheffield, England, fans can't wait to get their hands on the precious tickets. Due to the large influx of people, the organizers ask you to write a program for selling tickets, taking into account the following price list:

Quarterfinal
Semi-final
Final
Standard
55.50 £/per
75.88 £/per
110.10 £/per
Premium
105.20 £/per
125.22 £/per
160.66 £/per
VIP
118.90 £/per
300.40 £/per
400 £/per
When buying a ticket, the viewer can choose an option, a photo with the trophy, at a price of 40 pounds.
When you reach a certain amount, there are discounts:
    • Over 4000 pounds have a 25% discount and free photos with the trophy (if the photo option is turned on, the 40-pound ticket fee is not included)
    • Over 2500 pounds have a 10% discount
If the trophy photo option is selected, the price is charged after the discounts are calculated.
Input
'''
championship = input()
ticket_type = input()
number_of_tickets = int(input())
photo_thropy = input()

price = 0.0

if championship == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50 * number_of_tickets
    elif ticket_type == "Premium":
        price = 105.20 * number_of_tickets
    elif ticket_type == "VIP":
        price = 118.90 * number_of_tickets
elif championship == "Semi final":
    if ticket_type == "Standard":
        price = 75.88 * number_of_tickets
    elif ticket_type == "Premium":
        price = 125.20 * number_of_tickets
    elif ticket_type == "VIP":
        price = 300.40 * number_of_tickets
elif championship == "Final":
    if ticket_type == "Standard":
        price = 110.10 * number_of_tickets
    elif ticket_type == "Premium":
        price = 160.66 * number_of_tickets
    elif ticket_type == "VIP":
        price = 400 * number_of_tickets

if price > 4000:
    price = (75 / 100) * price
elif price > 2500:
    price = (90/100) * price

if photo_thropy == "Y" and price <= 2500:
    price += 40 * number_of_tickets

print(f"{price:.2f}")