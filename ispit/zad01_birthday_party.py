'''
1. Birthday Party
For her daughter's birthday, Lucy has decided to organize a party and to invite all her daughter’s classmates. For this purpose, she decided to rent an entertainment hall for children, the rent of which you will receive as an input from the console. 
Write a program to help Lucy calculate what budget she will need, given the following information about the extras needed for the celebration:
    • Cake – its price is 20% of the hall rent
    • Drinks – their price is 45% less than the one of the cake
    • Entertainer – its price is 1/3 of hall rent
'''
hall_rent = float(input())

cake_price = (20 / 100) * hall_rent
drinks = (55 / 100) * cake_price
entertrainer = (1/3) * hall_rent

budget = hall_rent + cake_price + drinks + entertrainer

print(budget)