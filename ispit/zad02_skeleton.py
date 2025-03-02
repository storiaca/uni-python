'''
2. Skeleton
The skeleton athlete Malcolm Davidson is fighting for an Olympic quota. You have the honor of writing the program that will calculate whether he earns a quota.
The program receives the control in minutes that must be reached or improved in order for Malcolm to make the quota. Also, the program will get the distance of the chute in meters, and the time in seconds for it to travel 100 meters.
It should be kept in mind that due to the slope of the chute, his time is decreased by 2.5 seconds every 120 meters. 
Input
Read 4 lines from the console:
Line 1. Control minutes – an integer in the range [0…59]
Line 2. Seconds for control – an integer in the range [0…59]
Line 3. The length of the chute in meters – a floating-point number in the range [0.00…50000]
  Line 4. Seconds for 100 meters– an integer in the range [0…1000]
'''
minutes = int(input())
seconds = int(input())
length_chute = float(input())
seconds_100_meters = int(input())

control_seconds = minutes * 60 + seconds
time_decrease = length_chute / 120
total_time_decrease = time_decrease * 2.5
malcolm_time = (length_chute / 100) * seconds_100_meters - total_time_decrease

if malcolm_time <= control_seconds:
    print(f"Malcolm Davidson won an Olympic quota!")
    print(f"His time is {malcolm_time:.3f}.")
else:
    print(f"No, Malcolm failed! He was {(malcolm_time - control_seconds):.3f} second slower.")