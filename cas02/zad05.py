'''
5. Supplies for School
The school year has already started and the head of the 10B class - Sophie has to buy a certain number of packets of pens, packets of markers, and detergent for cleaning the board. She is a regular customer of a bookstore, so there is a discount for her, which is a percentage of the total. Write a program that calculates how much money Sophie will have to raise to pay the bill, keeping in mind the following price list:
    • Package of pens- 5.80 USD. 
    • Package of markers - 7.20 USD. 
    • Detergent- 1.20 USD (for liter)
'''
pack_pens = int(input())
pack_markers = int(input())
liter_detergent = int(input())
percentage_reduction = int(input())

price_pens = 5.80
price_markers = 7.20
price_detergents = 1.20

discount_per = percentage_reduction / 100

all_price_pens = pack_pens * price_pens
all_price_markers = pack_markers * price_markers
all_price_detergents = liter_detergent * price_detergents

price_all_products = all_price_pens + all_price_markers + all_price_detergents

all_price_discount = price_all_products - (price_all_products * discount_per)

print(all_price_discount)
