'''
5. Godzilla vs. Kong
Filming for the long-awaited film "Godzilla vs. Kong" begins. Screenwriter Adam Wingard asks you to write a program to calculate whether the funds provided are enough to shoot the film. The photos will require a certain number of extras, clothing for each extra, and decor.
It is known that:
    • The set for the film is worth 10% of the budget. 
    • For more than 150 extras, there is a 10% discount on clothing.
'''
movie_budget = float(input())
number_extras = int(input())
price_cloth_per_extra = float(input())


# cena seta, postavke okruzenja za film je 10 posto budzeta
price_set =  (10/100) * movie_budget

price_clothing = number_extras * price_cloth_per_extra
# ako imamo vise od 150 ljudi, onda dobijamo 10 posto popusta na odelo
if (number_extras > 150):
    # 100 - 10 = 90 posto cene odela koju treba da platimo
    price_clothing = (90/100) * price_clothing

# ukupno treba da platimo set i odela
payment = price_set + price_clothing

if (movie_budget >= payment):
    print("Action!")
    print(f"Wingard starts filming with {(movie_budget - payment):.2f} USD left.")
else: # inace, movie_budget < payment
    print("Not enough money!")
    print(f"Wingard needs {(payment - movie_budget):.2f} USD more.")