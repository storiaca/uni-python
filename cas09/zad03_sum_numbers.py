'''
3. Sum Numbers
Write a program that reads an integer from the console and on each following line integers until their sum is greater than or equal to the original number. When the reading is finished, print the sum of the entered numbers.
'''
num = int(input())

total_num = 0

while True:
    if total_num >= num:
        break
    data = int(input())
    total_num += data

print(total_num)