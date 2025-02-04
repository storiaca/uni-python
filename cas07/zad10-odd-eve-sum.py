'''
10. Odd Even Sum 
Write a program that reads n number of integers given by the user and checks whether the sum of the numbers in even positions is equal to the sum of the numbers in odd positions.
    • If the sums are equal print two lines: "Yes" and on a new line "Sum = " + sum; 
    • If the sums are not equal print two lines: "No" and on a new line "Diff = " + the difference; 
The difference is calculated by absolute value. 
'''
n = int(input())

sum_odd = 0
sum_even = 0
for i in range(n):
    number = int(input())
    if(i%2 == 0):
        sum_even += number
    elif i % 2 !=0:
        sum_odd += number
if(sum_odd == sum_even):
    print('Yes')
    print(f'Sum = {sum_odd}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')