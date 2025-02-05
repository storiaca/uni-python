r = {
    10: 5,
    50: 10,
    400: 15,
    720: 16
}

# {"Marko Markovic": 4.56, "Sara Ivanovic": 5.00, "Tamara Ilic": 3.50}
b = int(input())
# get ce nam vratiti sve vrednosti iz r koje unesemo u b, ako je nema vratice 100
a = r.get(b, 100)

print(a) # unesemo 10 dobijemo 5, unesemo 400 dobijemo 15 itd