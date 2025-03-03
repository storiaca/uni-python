'''
Movie Stars
The accountant of the "Star City" cinema center hires you to write a program that calculates the salaries of the actors. Each production has a budget for actors. Until the "ACTION" command is given, you will receive the name of the actor and their salary. If the actor's name is longer than 15 characters, their salary will be 20% of the remaining budget at that point. If the budget runs out at any point, the program should stop.
Input
First, read one line from the console:
    • Budget for actors – a floating-point number in the range [1000.0... 2 100 000.0]
Then one or two lines are read repeatedly until the command "ACTION" or until the budget runs out:
    • Actor`s name – a string
If the actor name contains less than or equal to 15 characters: 
        ◦ Salary – a floating-point number in the range [250.0… 1 000 000.0]
'''
budget = float(input())

actor = input()
while actor != "ACTION":
    if len(actor) > 15:
        salary = 0.2 * budget
    else:
        salary = float(input())
    budget -= salary
    if budget < 0:
        break
    actor = input()
if budget >= 0:
    print(f"We are left with {budget:.2f} USD.")
else:
    print(f"We need {abs(budget):.2f} USD for our actors.")