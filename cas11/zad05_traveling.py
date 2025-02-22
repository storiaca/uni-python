'''
5. Traveling
Annie loves to travel and wants to visit several different destinations this year. When she chooses a destination, she will decide how much money she will need to get there and start saving. When she has saved enough, she will be able to travel.
Each time, the console will first read the destination and the minimum budget (a floating-point number) that will be needed for the trip.
Then several sums (floating-point numbers) will be read that Annie saves by working and when she manages to save enough for the trip, she will leave, and it should be printed on the console:
"Going to {destination}!" 
When she has visited all the destinations she wants, instead of a destination she will enter "End" and the program will end.
'''
destination = input()

while (destination != "End"):
    money = float(input())
    saved_money = 0
    while (saved_money < money):
        saved_money += float(input())
    print(f"Going to {destination}!")
    destination = input()