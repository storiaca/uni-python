'''
3. Combinations
Write a function that calculates how many solutions in natural numbers (including zero) have the equation:
'''
num = int(input())
result = 0
for i in range(0, num + 1):
    for j in range (0, num + 1):
        for z in range (0, num + 1):
            if (i + j + z == num):
                result +=1
print(result)

# drugi nacin bez jednog for loop-a

num = int(input())
result = 0
for i in range(0, num + 1):
    for j in range (0, num + 1):
        z = num - (i + j)
        if (0 <= z <= num):
            result +=1
print(result)