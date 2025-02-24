'''
2. Equal Sums Even Odd Position
Write a program that reads two six-digit integers from the console. The first entered number will always be smaller than the second one. Print on the console on 1 line separated by a space, all numbers that lie between the two numbers read from the console and satisfy the condition that the sum of the digits at the even and odd positions are equal. If there are no numbers meeting the condition no result is output on the console.
'''
num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1): # ovo su svi brojevi izmedju num1 i num2
    num_string = str(i) # pretvaramo posmatrani broj u string
    sum_odd = 0 # suma cifara na parnim pozicijama
    sum_even = 0 # suma cifara na neparnim pozicijama

    for j in range(0, len(num_string)):
        if j % 2 == 0:
            sum_even += int(num_string[j]) # 1597 num_string[0] = '1'
        else:
            sum_odd += int(num_string[j])
    if sum_even == sum_odd:
        print(num_string, end=" ")