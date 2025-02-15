'''
6. Max Number 
Write a program that, until it receives the "Stop" command, reads integers entered by the user, finds the largest among them, and prints it. One number is entered per line.
'''

num = ""
number_max = -9999999999999
while True:
    num = input()
    if num == "Stop":
        break

    num = int(num)
    if number_max < num:
        number_max = num
print(number_max)