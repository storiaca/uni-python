for i in range(1, 10, 2): # 1 3 5 7 9
    print(i)

# sa while petljom primer
i = 1

while(i<10): # 1 3 5 7 9
    print(i)
    i+=2

# drugi primer
a = 5
while a <= 10: # a = 5 a=6 a=7 itd do a=10
    print("a = " + str(a))
    a += 1

# primer sa for
for a in range(5, 11, 1):
    print("a = " + str(a))

# petlja radi dok god unosimo tekst koji nije "Stop"
tekst = input()
while (tekst != "Stop"):
    print("Loop")
    tekst = input()

# nacin da prekinemo petlju
while True:
    linija = input()
    if linija == "Stop":
        break