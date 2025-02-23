'''
1. Number Pyramid
Write a function that receives an integer n, entered by the user, and prints a pyramid of numbers as in the examples. 
'''
num = int(input())
curr = 1
is_curr_bigger_than_num = False

for i in range(1, num + 1):
    for j in range(1, i + 1):
        if curr > num:
            is_curr_bigger_than_num = True
            break
        print(str(curr) + ' ', end='')
        curr += 1
    if is_curr_bigger_than_num:
        break
    print()      