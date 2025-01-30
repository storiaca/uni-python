'''
    2. Bonus Score
An integer is given - the starting number of points. Bonus points are added to it according to the rules described below. Write a program that calculates the bonus points received by the number and the total number of points (number + bonus).
    • If the number is up to 100 inclusive, the bonus points are 5.
    • If the number is greater than 100, the bonus points are 20% of the number.
    • If the number is greater than 1000, the bonus points are 10% of the number.

    • Additional bonus points (added separately from the previous ones):
        ◦ For an even number  + 1 point.
        ◦ For a number ending in 5  + 2 points.
'''
number = int(input())
bonus = 0.0

if number <= 100:
     bonus = 5.0
elif number > 1000:
    bonus = number * 0.1
else:
    bonus = number * 0.2

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)