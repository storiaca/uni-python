'''
6. Cake
You're invited to a 30th birthday party, where the birthday boy serves a huge cake. However, he doesn't know how many pieces the guests can take from it. Your task is to write a program that calculates the number of pieces the guests have taken before it is eaten. You will receive the dimensions of the cake (width and length – integers) and then on each line until you receive the "STOP" command or until the cake is finished, the number of pieces the guests take from it. Each piece of cake is 1x1 cm.
Print one of the following lines on the console:
    • "{number of pieces} pieces are left." - if you receive STOP and have not finished the cake pieces
'''
w = int(input())
l = int(input())

num_pieces = w * l
piece = 0

while num_pieces >= 0:
    take = input()
    if take == "STOP":
        break

    num_pieces -= int(take)
    piece += 1


if num_pieces > piece:
    print(f"{num_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(num_pieces)} pieces more.")