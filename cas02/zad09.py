'''
9. Fish Tank
For his birthday, Steven received an aquarium in the shape of a parallelepiped. Initially, we read from the console in separate rows its dimensions - length, width, and height in centimeters. It is necessary to calculate how many liters of water the aquarium will collect if it is known that a certain percentage of its capacity is occupied by sand, plants, heater, and pump.
One liter of water is equal to one cubic decimeter / 1l = 1 dm3 /.
Write a program that calculates the liters of water needed to fill the aquarium.
'''

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

occupied_space = percentage / 100

aqua_volume = length * width * height
aqua_volume_litters = aqua_volume / 1000

reqired_liters = aqua_volume_litters * (1 - occupied_space)

print(reqired_liters)