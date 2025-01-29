'''
7. Hotel Room
The hotel offers 2 types of rooms: studio and apartment. Write a program that calculates the price for the entire stay for a studio and apartment. Prices depend on the month of stay:
'''
month = input()
number_of_nights = int(input())

price_studio = 0.00
price_apartment = 0.00

if((month == "May") or (month == "October")):
    price_studio = number_of_nights * 50
    price_apartment = number_of_nights * 65
    if(7 < number_of_nights < 14):
        price_studio = (95/100) * price_studio
    elif(number_of_nights > 14):
        price_studio = (70/100) * price_studio
        price_apartment = (90 / 100) * price_apartment

    print(f'Apartment: {price_apartment:.2f} USD.')
    print(f'Studio: {price_studio:.2f} USD.')
elif ((month == "June") or (month == "September")):
    price_studio = number_of_nights * 75.20
    price_apartment = number_of_nights * 68.70
    if (number_of_nights > 14):
        price_studio = (80 / 100) * price_studio
        price_apartment = (90 / 100) * price_apartment

    print(f'Apartment: {price_apartment:.2f} USD.')
    print(f'Studio: {price_studio:.2f} USD.')
elif ((month == "July") or (month == "August")):
    price_studio = number_of_nights * 76
    price_apartment = number_of_nights * 77
    if (number_of_nights > 14):
        price_apartment = (90 / 100) * price_apartment

    print(f'Apartment: {price_apartment:.2f} USD.')
    print(f'Studio: {price_studio:.2f} USD.')