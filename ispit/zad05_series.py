'''
You are hired by a television company to write a program that will calculate whether the customers will be able to buy the desired TV series. You have a budget and a number of TV series that the customer wants to purchase. Each TV series has a title and a price.
Some of the series have a discount:
    • Thrones – 50%
    • Lucifer – 40%	
    • Protector – 30%
    • TotalDrama – 20%
    • Area – 10%
Input
Read from the console:
    • Budget  - a floating-point number in the range [10.0… 100.0]
    • Number of series - n – a positive integer in the range [1… 10]
Read two lines for every movie series:
    • Name – a string
    • Price -  an integer in the range [1.0… 15.0]
'''
budget = float(input())
num_of_series = int(input())

total_price = 0
for i in range(num_of_series):
    name_series = input()
    price = int(input())

    if name_series == "Thrones":
        price = (50/100) * price
    elif name_series == "Lucifer":
        price = (60/100) * price
    elif name_series == "Protector":
        price = (70/100) * price
    elif name_series == "TotalDrama":
        price = (80/100) * price
    elif name_series == "Area":
        price = (90/100) * price
    total_price += price

if budget >= total_price:
    print(f"You bought all the series and left with {budget - total_price:.2f} USD.")
else:
    print(f"You need {total_price - budget:.2f} USD. more to buy the series!")