'''
2. Half Sum Element
Write a program that reads n number of integers entered by the user and checks if among them exists a number that is equal to the sum of all others.
    • If there are such an element print "Yes" and on a new line "Sum = " + its value
    • If there are no such element print "No" and on a new line "Diff = " + the difference between the largest element and the sum of the others (by absolute value)
'''
num = int(input())

max_num = -99999999999
sum_num = 0
for i in range(num):
    x = int(input())
    if(x > max_num):
        max_num = x
    sum_num += x
    
# da li je suma preostalix brojeva jednaka maksimumu
if(sum_num - max_num == max_num):
    print('Yes')
    print(f"Sum = {max_num}")
else:
    print('No')
    sum_num =  sum_num - max_num
    print(f"Diff = {abs(max_num - sum_num)}")
