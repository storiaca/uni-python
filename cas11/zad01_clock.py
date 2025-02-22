'''
1. Clock
Write a function that prints the hours of the day from 0:0 to 23:59, each on a separate line. The hours must be printed in the format "{hours}:{minutes}".
'''
for h in range(24):
    for m in range(60):
        print(f"{h}:{m}")