'''
4. Toy Shop
Sophie has a toy store. She receives a large order that she must fulfill. With the money she will earn, she wants to go on a trip. 
'''
price_travel = float(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

total_price = number_puzzle * puzzle + number_dolls * talking_doll + number_bears * teddy_bear + number_minions * minion + number_trucks * truck
total_number = number_trucks + number_bears + number_dolls + number_minions + number_puzzle

if(total_number >= 50):
    total_price = (75/100) * total_price

total_price = (90/100) * total_price

if(total_price >= price_travel):
    print(f'Yes! {(total_price - price_travel):.2f} USD left.')
else:
    print(f'Not enough money! {(price_travel -  total_price):.2f} USD needed.')

