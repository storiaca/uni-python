'''
5. Numbers from 100 to 200
Write a program that reads an integer entered by the user and checks if it is below 100, between 100 and 200 or above 200. If the number is:
    • below 100 print: "Less than 100"
    • between 100 and 200 print: "Between 100 and 200"
    • above 200 print: "Greater than 200"
'''
number = int(input())

if number < 100:
    print('Less than 100')
elif number <=200:
    print('Between 100 and 200')
elif number > 200:
    print('Greater than 200')