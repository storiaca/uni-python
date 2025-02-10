'''
    4. Walking
Emma wants to start a healthy lifestyle and has set a goal to walk 10,000 steps every day. However, some days she is very tired from work and will want to get home before she reaches her goal. Write a program that reads from the console how many steps she walks each time she goes out during the day, and when she reaches her goal, print "Goal reached! Good job!" and how many more steps she has walked "{difference between steps} steps over the goal!"
If she wants to go home before then, she will enter the command "Going home" and enter the steps she has walked while going home. Then, if she has failed to reach her goal, the console should print: "{difference between steps}  more steps to reach the goal."
'''
goal = 10000  # 10,000 steps 
steps = 0
while steps < goal:
    command = input()
    if command == "Going home":
        steps += int(input())
        break
    steps += int(command)     

if steps >= goal:
    print("Goal reached! Good job!")
    print(f"{steps - goal} steps over the goal!") 
else: 
    print(f"{goal - steps} more steps to reach the goal.")