'''
1. Fruit Market
Sophie decides to go on a diet and goes to a nearby market to buy strawberries, bananas, oranges, and raspberries. On the console, the price of strawberries in USD/kg and the amount of bananas, oranges, raspberries, and strawberries she needs to buy are entered. Write a program that calculates how much money she needs to pay the bill, knowing that:
    • The price of the raspberries is half the price of the strawberries.
    • The price of the oranges is 40% lower than the price of the raspberries.
    • Thepr price of bananas is 80% lower than the price of raspberries.
Input Data
Read 5 lines from the console:
    1. Price of strawberries in USD – a floating-point number in the range [0.00 … 10000.00]
    2. The number of bananas in kilograms – a floating-point number in the range [0.00 … 1 0000.00]
    3. The number of oranges in kilograms – a floating-point number in the range [0.00 … 10000.00]
    4. The number of raspberries in kilograms – a floating-point number in the range [0.00 … 10000.00]
    5. The number of strawberries in kilograms – a floating-point number in the range [0.00 … 10000.00]
'''
price_strawberries = float(input())
num_b = float(input())
num_o = float(input())
num_r = float(input())
num_s = float(input())

# Price of raspberries
price_r = (1/2) * price_strawberries

# ako je x 3/4 onda je y x=(3/4)*y

# The price of the oranges is 40% lower than the price of the raspberries.
# 40% posto niza => 100 - 40 = 60% znaci da je price_o 60% od price_r
price_o = (60/100) * price_r

# ako je x 75% posto od y onda je x = (75/100)*y
# ako je x 35% posto od y onda je x = (35/100)*y

# ako je x 45% niza(jeftinija) vrednost od y, onda je: 100-45=55, x = (55/100)*y
# ako je x 17% visa(skuplja) vrednost od y onda je: 100+17=115, x = (117/100)*y

# The price of bananas is 80% lower than the price of raspberries.
# 100 - 80 = 20
price_b = (20/100) * price_r

total_price = price_strawberries * num_s + price_r * num_r + price_b * num_b + price_o * num_o

print(f"{total_price:.2f}")

import math
minutes = int(input())
seconds = int(input())
length_chute = float(input())
seconds_100_meters = int(input())

control_seconds = minutes * 60 + seconds
time_decrease = length_chute / 120
total_time_decrease = time_decrease * 2.5
malcolm_time = (length_chute / 100) * math.floor(time_decrease) - total_time_decrease

if malcolm_time <= control_seconds:
    print(f"Malcolm Davidson won an Olympic quota!")
    print(f"His time is {malcolm_time:.3f}.")
else:
    print(f"No, Malcolm failed! He was {(malcolm_time - control_seconds):.3f} second slower.")


