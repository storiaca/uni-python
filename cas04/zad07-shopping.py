'''
Shopping
Peter wants to buy N video cards, M CPUs, and P number of RAM. If the number of video cards is greater than that of the processors, he receives a 15% discount on the final bill. The following prices apply:
    • Video card - 250 USD for one.
    • CPU - 35% from the total price of purchased video cards.
    • RAM - 10% from the total price of purchased video cards.
Calculate the amount needed to purchase the materials and calculate whether the budget will be enough.
'''
budget = float(input())
num_video_cards = int(input())
num_cpu = int(input())
num_ram = int(input())

price_video_card = 250 * num_video_cards

price_cpu = ((35/100) * price_video_card) * num_cpu
price_ram = ((10/100) * price_video_card) * num_ram

total_price = price_video_card + price_ram + price_cpu

if(num_video_cards > num_cpu):
    total_price = (85/100) * total_price

if(budget >= total_price):
    print(f'You have {(budget - total_price):.2f} USD left!')
else:
    print(f'Not enough money! You need {(total_price - budget):.2f} USD more!')