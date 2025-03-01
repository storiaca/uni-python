'''
. Easter Eggs Battle
On Easter, Sophie’s family gathers and she decides to organize a "battle" between Easter eggs. The rules of the "battle" are as follow:
    • Two players participate
    • Each of them starts with a certain number of eggs
    • When receiving the command "one" -> the first player wins => the eggs of the second decrease by one 
    • When receiving the command "two" -> the second player wins => the eggs of the first decrease by one
    • The game ends if one of the players runs out of eggs or until the "End" command is received
'''
eggs1 = int(input())
eggs2 = int(input())

linija = ""

while True:
    if eggs1 == 0:
        print(f"Player one is out of eggs. Player two has {eggs2} eggs left.")
        break
    if eggs2 == 0:
        print(f"Player two is out of eggs. Player one has {eggs1} eggs left.")
        break
    linija = input()
    if linija == "End":
        print(f"Player one has {eggs1} eggs left.")
        print(f"Player two has {eggs2} eggs left.")
        break
    if(linija == "one"):
        eggs2 -= 1
    elif linija == "two":
        eggs1 -= 1
