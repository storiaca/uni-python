'''
6. Food Delivery
The restaurant opens its doors and offers several menus at preferential prices: 
    • Chicken menu – 10.35 USD. 
    • Fish menu – 12.40 USD. 
    • Vegetarian menu – 8.15 USD. 
The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery).
The delivery price is 2.50 USD and is finally charged. 
'''
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_price = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_menu_total = chicken_menu * chicken_menu_price
fish_menu_total = fish_menu * fish_menu_price
vegan_menu_total = vegan_menu * vegan_menu_price

total_menu_price = chicken_menu_total + fish_menu_total + vegan_menu_total
dessert_price = (20 / 100) * total_menu_price

total_order_price = total_menu_price + dessert_price + delivery_price

print(total_order_price)