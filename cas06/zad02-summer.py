'''
2.  Summer Outfit
During the summer, the weather is often changing, and Steven needs your help. Write a program that, depending on the time of day and the degrees, can recommend to Steven what clothes to wear. Your friend has different plans for each stage of the day, which require a different look, you can see them on the table.
2 rows are read from the console:
    • Degrees - an integer in the range [10…42]
    • Time of the day - "Morning", "Afternoon", "Evening" (string)
'''
degrees = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")