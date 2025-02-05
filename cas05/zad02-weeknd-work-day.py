'''
2. Weekend or Working Day
Write a program that reads the day of the week (string) - entered by the user. If the day is a working day, it prints on the console - "Working day", if it is a day off - "Weekend". If any text other than the day of the week is entered, print "Error".
'''
user_day = input()

day = ''

if user_day == 'Monday':
  dan = 'Working day'
elif user_day == 'Tuesday':
  dan = 'Working day'
elif user_day == 'Wednesday':
  dan = 'Working day'
elif user_day == 'Thursday':
  dan = 'Working day'
elif user_day == 'Friday':
  dan = 'Working day'
elif user_day == 'Saturday':
  dan = 'Weekend'
elif user_day == 'Sunday':
  dan = 'Weekend'
else:
  dan = 'Error'

print(dan)