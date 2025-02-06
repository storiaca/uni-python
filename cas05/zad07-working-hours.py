'''
7. Working Hours
Write a program that reads an hour of the day (integer) and a day of the week (string) - entered by the user and checks whether the company's office is open, the office hours are from 10:00(10 am) to 18:00(6 pm), from Monday to Saturday including.
'''
hour = int(input())
day = input()

work_output = ""
if 10 <= hour <= 18:
    if day == 'Monday':
        work_output = "open"
    elif day == 'Tuesday':
        work_output = "open"
    elif day == 'Wednesday':
        work_output = "open"
    elif day == 'Thursday':
        work_output = "open"
    elif day == 'Friday':
        work_output = "open"
    elif day == 'Saturday':
        work_output = "open"
    elif day == 'Sunday':
        work_output = "closed"
else:
    work_output = "closed"
print(work_output)