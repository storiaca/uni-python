'''
    11. Fruit Shop
Fruit shop on weekdays works at the following prices:
fruit
banana
apple
orange
grapefruit
kiwi
pineapple
grapes
price
2.50
1.20
0.85
1.45
2.70
5.50
3.85
On Saturdays and Sundays, the store is works at higher prices:
fruit
banana
apple
orange
grapefruit
kiwi
pineapple
grapes
price
2.70
1.25
0.90
1.60
3.00
5.60
4.20
Write a program that reads from the console fruit (banana / apple / orange / grapefruit / kiwi / pineapple / grapes), day of the week (Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday), and quantity (a floating-point number), entered from the customer, and calculates the sum according to the prices in the tables above. In case of an invalid day of the week or invalid fruit name, print "error". Print the result rounded to the second decimal place.
'''
fruit = input()
day = input()
quantity = float(input())

#price = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        print(f'{(2.50 * quantity):.2f}')
    elif fruit == "apple":
        # price = 1.20 * quantity
        print(f'{(1.20 * quantity):.2f}')
    elif fruit == "orange":
       # price = 0.85 * quantity
        print(f'{(0.85 * quantity):.2f}')
    elif fruit == "grapefruit":
        #price = 1.45 * quantity
        print(f'{(1.45 * quantity):.2f}')
    elif fruit == "kiwi":
        #price = 2.70 * quantity
        print(f'{(2.70 * quantity):.2f}')
    elif fruit == "pineapple":
       # price = 5.50 * quantity
        print(f'{(5.50 * quantity):.2f}')
    elif fruit == "grapes":
        #price = 3.85 * quantity
        print(f'{(3.85 * quantity):.2f}')
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
       # price = 2.70 * quantity
        print(f'{(2.70 * quantity):.2f}')
    elif fruit == "apple":
        #price = 1.25 * quantity
        print(f'{(1.25 * quantity):.2f}')
    elif fruit == "orange":
       # price = 0.90 * quantity
        print(f'{(0.90 * quantity):.2f}')
    elif fruit == "grapefruit":
        #price = 1.60 * quantity
        print(f'{(1.60 * quantity):.2f}')
    elif fruit == "kiwi":
        #price = 3.00 * quantity
        print(f'{(3.00 * quantity):.2f}')
    elif fruit == "pineapple":
        #price = 5.60 * quantity
        print(f'{(5.60 * quantity):.2f}')
    elif fruit == "grapes":
        #price = 4.20 * quantity
        print(f'{(4.20 * quantity):.2f}')
    else:
        print("error")
else:
    print("error")