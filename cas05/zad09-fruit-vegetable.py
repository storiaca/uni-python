'''
9. Fruit or Vegetable
Write a program that reads a product name entered by the user and checks if it is a fruit or vegetable.
    • The fruits are banana, apple, kiwi, cherry, lemon, and grapes
    • The vegetables "vegetable" are tomato, cucumber, pepper, and carrot
    • Everything else is "unknown"
Print "fruit", "vegetable" or "unknown" depending on the introduced product. 
'''
product_name = input()

if product_name == "banana" or product_name == "apple" or product_name == "kiwi" or product_name == "cherry" or product_name == "lemon" or product_name == "grapes":
    print("fruit")
elif product_name == "tomato" or product_name == "cucumber" or product_name == 'pepper' or product_name == "carrot":
    print("vegetable")
else:
    print("unknown")

# drugi nacin sa recnikom

r = {
"banana": "fruit",
"apple": "fruit",
"kiwi": "fruit",
"cherry": "fruit",
"lemon": "fruit",
"grapes": "fruit",
"tomato": "vegetable",
"cucumber": "vegetable",
"pepper": "vegetable",
"carrot": "vegetable",
}

name_product = input()
product = r.get(name_product, "unknown")

print(product)

# resenje sa casa
namirnica = input()

if (namirnica == "banana" or namirnica == "apple" or
        namirnica=="kiwi" or namirnica == "cherry" or
        namirnica == "lemon" or namirnica == "grapes"):
    print("fruit")
elif (namirnica == "tomato" or namirnica == "cucumber" or namirnica == "pepper" or namirnica == "carrot"):
    print("vegetable")
else:
    print("unknown")
"""
drugi nacin
r = {
    "banana": "fruit",
    "apple": "fruit",
    "tomato": "vegetable"
}
print(r.get(namirnica, "unknown"))
"""

"""
napredno (koriste se liste)
voce = ["apple","banana","cherry", "lemon"]
povrce = ["tomato","carrot","pepper"]
if (namirnica in voce):
    print("fruit")
elif (namirnica in povrce):
    print("vegetable")
else:
    print("unknown")
"""