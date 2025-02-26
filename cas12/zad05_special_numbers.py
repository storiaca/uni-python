'''
5. Special Numbers
Write a program that reads a single integer N entered by the user and generates all possible "special" numbers from 1111 to 9999. For a number to be "special", it must meet the following condition:
    • N to be divisible by each of its digits without remainder.
'''
num = int(input())

for i in range(1111, 9999 + 1):
    num_test = str(i) # cim se pominje neki postupak sa ciframa
    # number je specijalan ako je num deljiv svim  njihovim ciframa

    special_number = True
    for j in num_test: # moguca je ovakva genericka petlja, ne treba nam pozicija
        # da se prolazi svim karakterima nekog stringa redom, u prvoj iteraciji je karakter
        # na poziciji 0, smesten u promenjljivu j
        if(int(j) == 0 or num % int(j) != 0):
            special_number = False
            break
    if(special_number):
        print(num_test, end=" ")