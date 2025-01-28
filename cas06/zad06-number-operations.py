'''
6. Operations Between Numbers
Write a program that reads two integers (N1 and N2) and an operator with which to perform a mathematical operation with them. Possible operations are: Addition (+), Subtraction (-), Multiplication (*), Division (/) and Division with remainder (%). When adding, subtracting, and multiplying the console, the result must be printed and whether it is even or odd. In ordinary division - the result. In modular division - the remainder. It should be borne in mind that the divisor can be equal to 0 (zero) and not divisible by zero. In this case, a specific message must be printed.
'''
n1 = int(input())
n2 = int(input())
operator = input()

if(operator == '+'):
    result = n1 + n2
    if(result % 2 == 0):
        print(f'{n1} + {n2} = {result} - even')
    else:
        print(f'{n1} + {n2} = {result} - odd')
elif(operator == '-'):
    result = n1 - n2
    if (result % 2 == 0):
        print(f'{n1} - {n2} = {result} - even')
    else:
        print(f'{n1} - {n2} = {result} - odd')
elif(operator == '/'):
    if((n2 > 0)):
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')
    else:
        print(f'Cannot divide {n1} by zero')
elif(operator == '*'):
    result = n1 * n2
    if (result % 2 == 0):
        print(f'{n1} * {n2} = {result} - even')
    else:
        print(f'{n1} * {n2} = {result} - odd')
elif(operator == '%'):
    if ((n2 > 0)):
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
    else:
        print(f'Cannot divide {n1} by zero')