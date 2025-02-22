'''
4. Sum of Two Numbers
Write a function that checks all possible combinations of a pair of numbers in the interval of two given numbers.
The output prints which in order is the first combination whose sum of the numbers equals a given magic number. 
If there is no combination matching the condition, a message is printed that none was found.
'''
num1 = int(input())
num2 = int(input())

magic_num = int(input())
count = 0
stop_loop = False

for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        count += 1
        if(i + j == magic_num):
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            stop_loop = True
            break
    if stop_loop:
        break
if (not stop_loop):
    print(f"{count} combinations - neither equals {magic_num}")
