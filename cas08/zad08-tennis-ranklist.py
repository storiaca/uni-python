'''
8. Tennis Ranklist 
Rafael Nadal is a tennis player whose next goal is to climb the world rankings in men's tennis. 
During the year, Nadal participates in a certain number of tournaments, and for each tournament, he receives points that depend on the position he finished in the tournament. There are three options for finishing a tournament:
    • W - if he is the winner, he receives 2000 points
    • F - if he is a finalist, he receives 1200 points
    • SF - if he is a semi-finalist, he receives 720 points
Write a program that calculates how many points Rafael Nadal will have after playing all the tournaments, knowing how many points he started the season with. Also, calculate how many points he earns on average from all tournaments played and what percentage of tournaments he has won.
'''
import math

number_tournaments = int(input())
number_points = int(input())

won_points = 0.00
total_points = 0
won_tournaments = 0
for i in range(number_tournaments):
    position = input()
    if(position == 'W'):
        won_points += 2000
        won_tournaments += 1
    elif (position == 'F'):
        won_points += 1200
    elif (position == 'SF'):
        won_points += 720
    total_points = number_points + won_points

print(f'Final points: {math.floor(total_points)}')
print(f'Average points: {int(won_points / number_tournaments)}')
print(f'{((won_tournaments / number_tournaments)*100):.2f}%')

# print(f'Average points: {math.floor(won_points / number_tournaments)}')