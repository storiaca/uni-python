'''
4. Food for Pets
Sophie has two pets - a dog and a cat. Write a program that prepares statistics on pet food for a certain number of days. Every day the dog and the cat eat a different amount of their shared food. Every third day they receive a prize - cookies. The amount of cookies is 10% of the total food eaten for the day. Your program should print statistics on the number of cookies they ate, what percentage of the original amount of total food they ate, and what percentage of the food the dog ate, and how much the cat ate.
'''
n = int(input())
total_food = float(input())
cookies = 0
total_eaten = 0
dog_eaten = 0
cat_eaten = 0

for day in range(1, n+1):
    dog = int(input())
    cat = int(input())

    if (day % 3 == 0): # da li je u pitanju svaki 3-ci dan
        cookies += (10/100) * (dog + cat)

    total_eaten += dog + cat
    dog_eaten += dog
    cat_eaten += cat

print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{((total_eaten/total_food)*100):.2f}% of the food has been eaten.")
print(f"{((dog_eaten/total_eaten)*100):.2f}% eaten from the dog.")
print(f"{((cat_eaten/total_eaten)*100):.2f}% eaten from the cat.")
