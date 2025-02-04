'''
9. Left and Right Sum
Write a program that reads 2 * n number of integers given by the user and checks if the sum of the first n numbers (left sum) is equal to the sum of the second n numbers (right sum). If equal, prints "Yes, sum = " + sum; otherwise prints "No, diff = " + diff. The difference is calculated as a positive number (in absolute value).
'''
n = int(input())

sum1 = 0
sum2 = 0

for i in range(n):
    number = int(input())
    sum1 += number

for j in range(n):
    number = int(input())
    sum2 += number

if(sum1 == sum2):
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {abs(sum1-sum2)}')