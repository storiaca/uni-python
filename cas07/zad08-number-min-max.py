'''
8. Number sequence
Write a program that reads n number of integers. Print the largest and the smallest number among the entered ones.
'''
n = int(input())

max_number = -999999999999999999
min_number = 99999999999999999999
for i in range(n):
    number = int(input())
    if(number > max_number):
        max_number = number
    if (number < min_number):
        min_number = number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')