'''
Movie Destination
The director of a major film production wants to know if the budget allocated to him will be enough to shoot the film. Help him by writing a program that calculates how much it will cost him to make the film, knowing how much a day of filming costs. The price for one day is determined by the season and the destination: 
'''
budzet = float(input())
destinacija = input()
sezona = input()
broj_dana = int(input())

cena_po_danu = 0
if(sezona == "Winter"):
    if destinacija == "Dubai":
        cena_po_danu += 45000
    elif destinacija == "Washington":
        cena_po_danu = 17000
    elif destinacija == "London":
        cena_po_danu = 24000
elif sezona == "Summer":
    if destinacija == "Dubai":
        cena_po_danu = 40000
    elif destinacija == "Washington":
        cena_po_danu = 12500
    elif destinacija == "London":
        cena_po_danu = 20250

ukupna_cena = broj_dana * cena_po_danu

if destinacija == "Dubai":
    # 30% popusta dobijamo na ukupnu cenu
    ukupna_cena = (70/100) * ukupna_cena

if destinacija == "Washington":
    # cena se povecava za 25%
    ukupna_cena = (125/100) * ukupna_cena

if budzet >= ukupna_cena:
    print(f"The budget for the movie is enough! We have {(budzet - ukupna_cena):.2f} USD left!")
else:
    print(f"The director needs {(ukupna_cena - budzet):.2f} USD more!")