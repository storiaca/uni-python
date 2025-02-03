'''
6. Oscars
You have been invited by the academy to write software that calculates the points for an actor/actress. The academy will give you initial points for the actor. Each assessor will then give their score. The points an actor gets are formed by: the length of the assessor's name multiplied by the points they give divided by two. 
If the score at any point exceeds 1250.5 the program must break and print that the given actor has received a nomination.
'''
actor_name = input()
academy_points = float(input())
n = int(input())

points_needed = 1250.5
break_loop = False

for i in range(n):
    if (academy_points > points_needed):
        break_loop = True
        break
    name = input()
    score = float(input())
    academy_points += (len(name) * score) / 2

if(break_loop or academy_points > points_needed):
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(points_needed - academy_points):.1f} more!')