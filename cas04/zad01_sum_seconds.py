'''
1. Sum Seconds
Three athletes finish in a matter of seconds (between 1 and 50). Write a program that reads the times of the competitors in seconds entered by the user and calculates their total time in the format "minutes:seconds". Display the seconds with leading zero (2  "02", 7  "07", 35  "35"). 
'''
import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')