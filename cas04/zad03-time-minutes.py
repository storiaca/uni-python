'''
3. Time + 15 Minutes
Write a program that reads the hour and minutes of the 24-hour day entered by the user and calculates what time it will be in 15 minutes. Print the result in hours:minutes. The hours are always between 0 and 23, and the minutes are always between 0 and 59. The hours are written in one or two digits. Minutes are always displayed in two digits, with a leading zero when necessary. 
'''
hours = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    minutes -= 60
    hours +=1
if hours >= 24:
    hours = 0

print(f'{hours}:{minutes:02d}')

