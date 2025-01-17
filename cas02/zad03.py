# Deposit Calculator
deposit = float(input())
month = int(input())
interest = float(input())

accured_interest = deposit * (interest / 100)
month_interest = accured_interest / 12
total_amount = deposit + (month * month_interest)

print(total_amount)