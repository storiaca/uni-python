'''
6. World Swimming Record
Oliver decides to break the World Record for long-distance swimming. On the console, we type: the record that Oliver has to break, the distance in meters he has to swim, and the time in seconds for which he swims a distance of 1 m. To write a program that calculates whether he has done the record, it must be considered that: the resistance of the water slows him down every 15 m by 12.5 seconds. After calculating how many seconds Oliver will slow down, the result should be rounded down to the nearest integer number.
Calculate the time in seconds for which Ivan will swim the distance and the difference from the World Record. 
'''
import math

record = float(input())
distance = float(input())
time_for_meter = float(input())

# a // b  je isto sto i math.floor(a/b)

time = distance * time_for_meter

# time += (distance // 15) * 12.5
# mora zato sto se koriste float tip brojevi
time += (math.floor(distance/15)) * 12.5

if(record > time):
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(time - record):.2f} seconds slower.')