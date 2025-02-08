for i in range(2, 10, 7): # 2,9
    print(i)

for i in range(5, 0): # nema rezultata, prazan opseg, kad je prvi broj veci od drugog
    print(i)

# ord('A') = 65, chr(65) = A, chr(97) = a
# i = 97 sto je jednako a, pa je i=98 sto je jednako b pa je i=99 sto je jednako c
for i in range(97, 100): # a b c
    print(chr(i))

# for i in range(0, 2, 0.5): # ovo je greska: TypeError: 'float' object cannot be interpreted as an integer
#    print(i) # znaci ne moze da bude float, mora da bude ceo broj u koraku

# takodje nula ne sme da bude u koraku
#for i in range(1,4,0): # ovo nije dozvoljeno zbog 0 u koraku, bice zauvek u petlji
#    print(i)s