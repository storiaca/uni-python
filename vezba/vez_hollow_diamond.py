'''
Hollow Diamond
Write a program that prints a hollow diamond pattern of 2n-1 rows. The pattern should be such that it has a hollow diamond in the center. The pattern should be similar to the one shown below.
'''
num_rows = int(input("Enter the number of rows: "))
for i in range(1, num_rows + 1):
    for j in range(num_rows - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(num_rows - 1, 0, -1):
    for j in range(num_rows - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")    

# Drugo resenje
n = 5
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print(j, end="")
        else:
            print(" ", end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()