'''
    4. Clever Lily
Lily is now N years old. For every birthday she receives a present. 
    • For the odd birthdays (1, 3, 5...n) she receives toys.
    • For the even birthdays (2, 4, 6...n) she receives money. 
For the second birthday, she receives 10.00 USD, and the amount increases by 10.00 USD for each following even birthday (2 -> 10, 4 -> 20, 6 -> 30...etc.). Over the years, Lily has been secretly saving this money. Lily's brother, in the years that she receives money, takes 1.00 USD of it. Lily sold the toys, she received over the years, for P USD each and added the amount to the saved money. With the money, she wanted to buy a washing machine for X USD. Write a program to calculate how much money she has collected and whether she has enough to buy a washing machine.
'''
age = int(input())
price_machine = float(input())
price_toy = int(input())

money = 0
toys = 0
money_per_birthday = 10

for i in range(1, age+1):
    if(i % 2 == 0): # parni rodjendan
        money += money_per_birthday - 1
        money_per_birthday += 10
    else: # neparni rodjendan
        toys += 1
total_money = money + (toys * price_toy)

if(total_money >= price_machine):
    print(f'Yes! {total_money - price_machine:.2f}')
else:
    print(f'No! {price_machine - total_money:.2f}')