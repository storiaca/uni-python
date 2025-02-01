'''
2. Numbers 1...N with Step 3
Write a program that reads a number n entered by the user and prints the numbers from 1 to n with step 3.
'''
n = int(input())

for num in range(1, n + 1, 3):
    print(f'{num}')