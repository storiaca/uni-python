'''
3. Histogram
There are n integers in the range [1...1000]. Of these, some percent p1
are below 200, another percent p2 are from 200 to 399, another percent p3
are from 400 to 599, another percent p4 are from 600 to 799 and the
remaining p5 percent are from 800 upwards. Write a program that
calculates and prints the percentages p1, p2, p3, p4, and p5.

Example: we have n = 20 numbers: 53, 7, 56, 180, 450, 920, 12, 7, 150,
250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65.
We get the following distribution and visualization:

Koliko procenata je 379 od 1000?
(x/100) * 1000 = 378
x = (379/1000) * 100

koliko procenata je 117 od 189
(117/189)*100

koliko procenata je 37 od 2800?
(37/2800)*100

koliko procenata je 1123 od 47
(1123/47)*100
'''
num = int(input())

opseg1 = 0
opseg2 = 0
opseg3 = 0
opseg4 = 0
opseg5 = 0

for i in range(num):
    broj = int(input())
    if(broj < 200):
        opseg1 += 1
    elif (200<= broj <= 399):
        opseg2 += 1
    elif (400<= broj <= 599):
        opseg3 += 1
    elif (600<= broj <= 799):
        opseg4 += 1
    elif (broj >= 800):
        opseg5 += 1

print(f'{((opseg1/num)*100):.2f}%')
print(f'{((opseg2/num)*100):.2f}%')
print(f'{((opseg3/num)*100):.2f}%')
print(f'{((opseg4/num)*100):.2f}%')
print(f'{((opseg5/num)*100):.2f}%')