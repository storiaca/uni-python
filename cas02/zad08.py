'''
8. Basketball Equipment
Jesse decides he wants to play basketball, but he needs equipment to train. Write a program that calculates what costs Jesse will have if he starts training, knowing how much the basketball training fee is for 1 year. Required equipment:
    • Sneakers – 40% less than the annual fee.
    • Outfit – 20% less than sneakers.
    • Ball – 25% of the outfit price.
    • Accessories – 20% of the ball price.
    iz dokuemntacije:
    • Basketball sneakers – their price is 40% less than the fee for one year
    • Basketball outfit – its price is 20% cheaper than the sneakers
    • Ball – its price is 1 / 4 of the price of the outfit
    • Basketball Accessories –its price is 1 / 5 of the price of the ball
'''

annual_fee = int(input())

sneakers = annual_fee - (annual_fee * (40 / 100))
outfit = sneakers - (sneakers * (20 / 100))
ball = outfit * (25 / 100)
accessories = ball * (20 / 100)

total_price = annual_fee + sneakers + outfit + ball + accessories

print(total_price)