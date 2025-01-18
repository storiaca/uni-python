# Fish Tank

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

occupied_space = percentage / 100

aqua_volume = length * width * height
aqua_volume_litters = aqua_volume / 1000

reqired_liters = aqua_volume_litters * (1 - occupied_space)

print(reqired_liters)