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

# resenje sa if-else
broj = int(input())

dan = ''

if broj == 1: 
  dan = 'Monday'
elif broj == 2: 
  dan = 'Tuesday'
elif broj == 3:
  dan = 'Wednesday'
elif broj == 4:
  dan = 'Thursday'
elif broj == 5:
  dan = 'Friday'
elif broj == 6:
  dan = 'Saturday'
elif broj == 7:
  dan = 'Sunday'
else: 
  dan = 'Error'

print(dan)