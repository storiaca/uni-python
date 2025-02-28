'''
write a program that reads an integer n from the standard input and prints a rectangle of size n x n. The rectangle should be filled with asterisks (*) and in middle be spaces. The rectangle should look like this:
'''
# n = int(input("Enter the size of the rectangle: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# Drugo resenje
n = int(input())  

for i in range(n):  
    if i == 0 or i == n - 1:  
        print("* " * n)  
    else:  
        print("* " + "  " * (n - 2) + "*")