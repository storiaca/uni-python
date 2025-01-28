'''
5. Journey
Strangely, most people plan their vacation early. A young programmer has an exact budget and free time for each season. Write a program that will accept the budget and the season, and print, where the programmer will rest and how much he will spend.
The budget determines the destination, and the season determines how much of the budget he will spend. If it is summer, he will rest at the campsite and in the winter at a hotel. If he is in Europe, he will stay in a hotel, regardless of the season. Each campsite or hotel, according to the destination, has its price that corresponds to a certain percentage of the budget:
'''
budget = float(input())
season = input()

destination = ''
accomodation = '' # Camp ili Hotel
money_spent = 0.00

if (budget <= 100):
    destination = 'Serbia'
    if (season == 'summer'):
        accomodation = 'Camp'
        money_spent = (30 / 100) * budget
    elif (season == 'winter'):
        accomodation = 'Hotel'
        money_spent = (70 / 100) * budget
elif (budget <= 1000):
    destination = 'Balkans'
    if (season == 'summer'):
        accomodation = 'Camp'
        money_spent = (40 / 100) * budget
    elif (season == 'winter'):
        accomodation = 'Hotel'
        money_spent = (80 / 100) * budget
elif (budget > 1000):
    destination = 'Europe'
    accomodation = 'Hotel'
    money_spent = (90 / 100) * budget

print(f'Somewhere in {destination}')
print(f'{accomodation} - {money_spent:.2f}')