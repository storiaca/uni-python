'''
Hourglass
Write a program that reads an integer n from the standard input and prints an hourglass of size n. An hourglass of size n is a shape that looks like this:
n = 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
'''
n = int(input("Enter the size of the hourglass: "))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")    

# Drugo resenje
n = int(input())

for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)
for i in range(2, n + 1):
    print(" "* (n - i) + "* " * i)