'''
5. Account Balance
Write a program that calculates how much total money is in a bank account after making a certain number of deposits. On each line, you will receive the amount you need to deposit into the account until you receive a "NoMoreMoney" command. For each amount received, the console should output "Increase: " + the amount and that amount should be added to the account. If a number less than 0 is received, the console should output "Invalid operation!" and the program should end. When the program ends, it should print "Total: " + the total amount in the account, formatted to two digits after the decimal point.
'''
total_amount = 0.00

line = ""
while True:
     line = input()

     if(line == 'NoMoreMoney'):
         print(f"Total: {total_amount:.2f}")
         break
     line = float(line)
     if line < 0:
         print("Invalid operation!")
         print(f"Total: {total_amount:.2f}")
         break
     total_amount += float(line)
     print(f"Increase: {float(line):.2f}")