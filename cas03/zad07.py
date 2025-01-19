'''
7. Area of Figures
Write a program in which the user enters the type and dimensions of a geometric figure and calculates its area. The figures are of four types: square, square, rectangle, circle, and triangle. The first line of the input reads the type of figure (string with the following options: square, rectangle, circle, or triangle).
    • If the figure is a square: on the next line read a floating-point number - the length of its side
    • If the figure is a rectangle: on the next two lines read two floating-point numbers - the lengths of its sides
    • If the figure is a circle: on the next line read a floating-point number - the radius of the circle
    • If the figure is a triangle: on the next two lines read two floating-point numbers - the length of its side and the length of the height to it
Round the result up to 3 digits after the decimal point.
'''
import math
figure = input()

if figure == 'square':
    dimensionOne: float = float(input())
    area = dimensionOne * dimensionOne
    print(f'{area:.3f}')
elif figure == 'rectangle':
    dimensionOne: float = float(input())
    dimensionTwo: float = float(input())
    area = dimensionOne * dimensionTwo
    print(f'{area:.3f}')
elif figure == 'circle':
    dimensionOne: float = float(input())
    area = (dimensionOne * dimensionOne) * math.pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    dimensionOne: float = float(input())
    dimensionTwo: float = float(input())
    area = (dimensionOne * dimensionTwo) * 0.5
    print(f'{area:.3f}')