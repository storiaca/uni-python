'''
10. Invalid Number
A number is valid if it is in the range [100… 200] or is 0. Write a program that reads an integer entered by the user and prints "invalid" if the number entered is not valid.
'''
number = int(input())

if 100 <= number <= 200 or number == 0:
    print("")
else:
    print("invalid")