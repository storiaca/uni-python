'''
    6. Repainting
Peter wants to repaint the living room and has hired craftsmen for this purpose. Write a program that calculates the cost of repairs, given the following prices:
    • Protective nylon - 1.50 USD per square meter
    • Paint - 14.50 USD for a liter
    • Paint thinner - 5.00 USD for a liter
Just in case, to the necessary materials, Peter wants to add another 10% of the amount of paint and 2 square meters of nylon, of course, 0.40 USD for bags. The amount paid to the masters for 1 hour of work is equal to 30% of the sum of all costs for materials.
'''
price_nylon = 1.50
price_paint = 14.50
price_paint_thinner = 5.00
bags = 0.4

nylon = int(input())
paint = int(input())
detergent = int(input())
hours = int(input())

sum_nylon = (nylon + 2) * price_nylon
sum_paint = (paint + (paint * 0.1)) * price_paint
sum_detergent = detergent * price_paint_thinner

total_sum_materials = sum_nylon + sum_paint + sum_detergent + bags
sum_workers = (total_sum_materials * 0.3) * hours

total_sum = total_sum_materials + sum_workers

print(f'{total_sum} USD')