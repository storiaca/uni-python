'''
    5. Small Shop
    1. An enterprising person opens neighbourhood shops in several cities and sells at different prices:
city / product
coffee
water
beer
sweets
peanuts
London
0.50
0.80
1.20
1.45
1.60
Rome
0.40
0.70
1.15
1.30
1.50
Paris
0.45
0.70
1.10
1.35
1.55
    2. Write a program that reads product (string), city (string), and quantity (a floating-point number) entered by the user and calculates and prints how much the corresponding quantity of the selected product costs in the specified city.
'''
product = input()
city = input()
quantity = float(input())

price = 0

if city == "London":
    if product == "coffee":
        price = 0.50 * quantity
    elif product == "water":
        price = 0.80 * quantity
    elif product == "beer":
        price = 1.20 * quantity
    elif product == "sweets":
        price = 1.45 * quantity
    elif product == "peanuts":
        price = 1.60 * quantity
elif city == "Rome":
    if product == "coffee":
        price = 0.40 * quantity
    elif product == "water":
        price = 0.70 * quantity
    elif product == "beer":
        price = 1.15 * quantity
    elif product == "sweets":
        price = 1.30 * quantity
    elif product == "peanuts":
        price = 1.50 * quantity
elif city == "Paris":
    if product == "coffee":
        price = 0.45 * quantity
    elif product == "water":
        price = 0.70 * quantity
    elif product == "beer":
        price = 1.10 * quantity
    elif product == "sweets":
        price = 1.35 * quantity
    elif product == "peanuts":
        price = 1.55 * quantity
print(price)