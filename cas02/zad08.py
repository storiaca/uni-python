'''
8. Basketball Equipment
Jesse decides he wants to play basketball, but he needs equipment to train. Write a program that calculates what costs Jesse will have if he starts training, knowing how much the basketball training fee is for 1 year. Required equipment:
'''

annual_fee = int(input())

sneakers = annual_fee - (annual_fee * (40 / 100))
outfit = sneakers - (sneakers * (20 / 100))
ball = outfit * (25 / 100)
accessories = ball * (20 / 100)

total_price = annual_fee + sneakers + outfit + ball + accessories

print(total_price)