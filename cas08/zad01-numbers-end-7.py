'''
1. Numbers Ending in 7
Write a program that prints the numbers in the range 1 to 1000 that end with 7
'''
for i in range(1, 1001):
    if (i % 10 == 7):
        print(i)