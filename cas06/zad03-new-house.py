'''
3. New House
John and Sophie are buying a house not far from Sofia. Sophie loves flowers so much that she convinces you to write a program that will calculate how much it will cost them, to plant a certain number of flowers and whether the available budget will be enough. Different flowers have different prices.
'''
type_flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0.0

if (type_flowers == "Roses"):
    price = number_of_flowers * 5.00

    if(number_of_flowers > 80):
       #  dobijamo popust od 10%, 100 - 10 = 90 posto cene ruza treba da platimo
       price =  (90/100) * price

elif (type_flowers == "Dahlias"):
    price = number_of_flowers * 3.80
    if(number_of_flowers > 90):
        # dobijamo popust od 15 posto, 100 - 15 = 85
        price = (85/100) * price

elif (type_flowers == "Tulips"):
    price = number_of_flowers * 2.80
    if (number_of_flowers > 80):
        # dobijamo popust od 15 posto, 100 - 15 = 85
        price = (85 / 100) * price

elif (type_flowers == "Narcissus"):
    price = number_of_flowers * 3.00
    if (number_of_flowers < 120):
        # cena raste za 15 posto, 100 + 15 = 115
        price = (115 / 100) * price

elif (type_flowers == "Gladiolus"):
    price = number_of_flowers * 2.50
    if (number_of_flowers < 80):
        # cena raste za 20 posto, 100 + 20 = 120
        price = (120 / 100) * price

if (budget >= price):
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flowers} and {(budget - price):.2f} USD left.")
else:
    print(f"Not enough money, you need {(price - budget):.2f} USD more.")