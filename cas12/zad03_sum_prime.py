'''
3. Sum Prime Non-Prime
Write a program that reads integers from the console until a "stop" command is received. Find the sum of all the entered prime numbers and the sum of all the entered non-prime numbers. Since by mathematical definition negative numbers cannot be prime, if the input is a negative number, display the following message "Number is negative." In this case, the entered number is ignored and is not added to either of the two sums, and the program continues its execution, waiting for another number to be entered. 
The output should print on two lines the two found sums in the following format:
    • "Sum of all prime numbers is: {prime numbers sum}"
    • "Sum of all non prime numbers is: {nonprime numbers sum}"
'''
line = ""
sum_prime = 0
sum_non_prime = 0

while True:
    line = input()
    if line == "stop":
        break
    num = int(line)

    if num < 0:
        print("Number is negative.")
        continue # returns on top of while
    if num == 1:
        sum_non_prime += 1
        continue # returns on top of while

    is_prime = True
    for i in range(2, num): # 2,3,4,5... num-1
        if (num % i == 0):
            is_prime = False
            break
    if(is_prime):
        sum_prime += num
    else:
        sum_non_prime += num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

# resenje sa if else
line = ""
sum_prime = 0
sum_non_prime = 0

while True:
    line = input()
    if line == "stop":
        break
    num = int(line)

    if num < 0:
        print("Number is negative.")

    elif num == 1:
        sum_non_prime += 1
    else:
        is_prime = True
        for i in range(2, num): # 2,3,4,5... num-1
            if (num % i == 0):
                is_prime = False
                break
        if(is_prime):
            sum_prime += num
        else:
            sum_non_prime += num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")