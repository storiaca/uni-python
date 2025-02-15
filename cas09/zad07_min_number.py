'''
7. Min Number
Write a program that, until it receives the "Stop" command, reads integers entered by the user, finds the least among them, and prints it. One number is entered per line.
'''
num = ""
number_min = 9999999999999  # 2**63-1
while True:
    num = input()
    if num == "Stop":
        break

    num = int(num)
    if number_min > num:
        number_min = num  # number_min = min(number_min, num) - alternativno  resenje     
print(number_min) # print(f"{number_min}") - alternativno resenje