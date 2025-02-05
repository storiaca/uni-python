'''
1. Day of Week
Write a program that reads an integer entered by the user and prints a day of the week within [1 ... 7] or prints "Error" if the number entered is invalid.
'''
r = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

num = int(input())

result = r.get(num, 'Error')

print(result)