'''
7. Trekking Mania
Climbers from all over the world gather in groups and mark the next peaks to climb. Depending on the size of the group, climbers will climb different peaks.
    • Group up to 5 people - climb Makalu
    • Group of 6 to 12 people - climb Mont Blanc
    • Group of 13 to 25 people - climb Kilimanjaro
    • Group of 26 to 40 people - climb K2
    • Group of 41 or more people - climb Everest
Write a function that calculates the percentage of climbers climbing each peak.
'''
number_of_groups = int(input())

climber1 = 0
climber2 = 0
climber3 = 0
climber4 = 0
climber5 = 0
total_people = 0
for i in range(number_of_groups):
    number_of_people = int(input())
    if(number_of_people <= 5):
        climber1 += number_of_people
    elif  6 <= number_of_people <= 12:
        climber2 += number_of_people
    elif 13 <= number_of_people <= 25:
        climber3 += number_of_people
    elif 26 <= number_of_people <= 40:
        climber4 += number_of_people
    elif number_of_people >= 41:
        climber5 += number_of_people

    total_people += number_of_people


print(f"{((climber1 / total_people) * 100):.2f}%")
print(f"{((climber2 / total_people) * 100):.2f}%")

print(f"{((climber3 / total_people) * 100):.2f}%")

print(f"{((climber4 / total_people) * 100):.2f}%")

print(f"{((climber5 / total_people) * 100):.2f}%")