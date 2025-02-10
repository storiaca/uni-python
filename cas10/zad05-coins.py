'''
5. Coins
Vending machine manufacturers wanted to make their machines return as few change coins as possible. Write a program that receives an amount - the change that needs to be returned and calculates with how few coins this can be done. The coins can be 2.00 EUR, 1.00 EUR, 0.50 EUR, 0.20 EUR, 0.10 EUR, 0.05 EUR, 0.02 EUR, 0.01 EUR.
'''
import math
change = float(input())

coins = 0

while (change > 2.00 or math.fabs(change-2.00) < 0.0000000001):
    coins += 1
    change -= 2.00

while (change > 1.00 or math.fabs(change-1.00) < 0.0000000001):
    coins += 1
    change -= 1.00

while (change > 0.50 or math.fabs(change-0.50) < 0.0000000001):
    coins += 1
    change -= 0.50

while (change > 0.20 or math.fabs(change-0.20) < 0.0000000001):
    coins += 1
    change -= 0.20

while (change > 0.10 or math.fabs(change-0.10) < 0.0000000001):
    coins += 1
    change -= 0.10

while (change > 0.05 or math.fabs(change-0.05) < 0.0000000001):
    coins += 1
    change -= 0.05

while (change > 0.02 or math.fabs(change-0.02) < 0.0000000001):
    coins += 1
    change -= 0.02

while (change > 0.01 or math.fabs(change-0.01) < 0.0000000001):
    coins += 1
    change -= 0.01

print(coins)