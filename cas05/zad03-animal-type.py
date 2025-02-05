'''
3. Animal Type
Write a program that prints the species of the animal according to its name entered by the user.
    1. dog -> mammal
    2. crocodile, tortoise, snake -> reptile
    3. others -> unknown
'''
user_input = input()

animal_type = ""

if user_input == 'dog':
    animal_type = 'mammal'
elif user_input == 'crocodile':
    animal_type = 'reptile'
elif user_input == 'tortoise':
    animal_type = 'reptile'
elif user_input == 'snake':
    animal_type = 'reptile'
else:
    animal_type = 'unknown'

print(animal_type)

# resenje sa recnikom
r = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
}

user_animal = input()

result = r.get(user_animal, 'unknown')

print(result)