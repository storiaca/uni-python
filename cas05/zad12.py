'''
12. Trade Commissions
'''
'''
if((city != "London" and grad != "Paris" and grad != "Rome") or (sales_volume < 0)):
    print('error')
else:
'''
city = input()
sales_volume = float(input())

if (city == "London"):
    if (0 <= sales_volume <= 500):
        print(f"{((5/100) * sales_volume):.2f}")
    elif (500 < sales_volume <= 1000):
        print(f"{((7 / 100) * sales_volume):.2f}")
    elif (1000 < sales_volume <= 10000):
        print(f"{((8 / 100) * sales_volume):.2f}")
    elif (sales_volume > 10000):
        print(f"{((12 / 100) * sales_volume):.2f}")
    else:
        print("error")

elif (city == "Paris"):
    if (0 <= sales_volume <= 500):
        print(f"{((4.5 / 100) * sales_volume):.2f}")
    elif (500 < sales_volume <= 1000):
        print(f"{((7.5 / 100) * sales_volume):.2f}")
    elif (1000 < sales_volume <= 10000):
        print(f"{((10 / 100) * sales_volume):.2f}")
    elif (sales_volume > 10000):
        print(f"{((13/ 100) * sales_volume):.2f}")
    else:
        print("error")

elif (city == "Rome"):
    if (0 <= sales_volume <= 500):
        print(f"{((5.5 / 100) * sales_volume):.2f}")
    elif (500 < sales_volume <= 1000):
        print(f"{((8 / 100) * sales_volume):.2f}")
    elif (1000 < sales_volume <= 10000):
        print(f"{((12 / 100) * sales_volume):.2f}")
    elif (sales_volume > 10000):
        print(f"{((14.5 / 100) * sales_volume):.2f}")
    else:
        print("error")
else:
    print("error")