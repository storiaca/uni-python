'''
6. Speed Info
Write a program that reads the speed (floating-point number) entered by the user and prints speed information. 
    • At speed up to 10 (inclusive) print "slow"
    • At speed between 10 and 50 (inclusive) print "average" 
    • At speed between 50 and 150 (inclusive) print "fast"
    • At speed between 150 and 1000 (inclusive) print "ultra fast" 
    • At a higher speed print "extremely fast"
'''
speed = float(input())

if speed <= 10:
    print('slow')
elif speed <= 50:
    print('average')
elif speed <= 150:
    print('fast')
elif speed <= 1000:
    print('ultra fast')
elif speed > 1000:
    print('extremely fast')