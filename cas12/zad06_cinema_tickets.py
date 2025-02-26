'''
6. Cinema Tickets
Your task is to write a program that calculates the percentage of tickets for each type of sold tickets: student, standard, and kid for all screenings. You also need to calculate what percentage of the hall is filled for each screening. 
'''
linija = ""

student = 0
standard = 0
kid = 0
ukupno_karti = 0

while True:
    linija = input()
    if linija == "Finish":
        print(f"Total tickets: {ukupno_karti}")
        print(f"{((student / ukupno_karti) * 100):.2f}% student tickets.")
        print(f"{((standard / ukupno_karti) * 100):.2f}% standard tickets.")
        print(f"{((kid / ukupno_karti) * 100):.2f}% kids tickets.")
        break
    naziv_filma = linija
    broj_slobodnih_mesta_u_sali = int(input())

    linija2 = ""
    broj_popunjenih_mesta = 0

    while True:
        linija2 = input()
        if(linija2 == "End"):
            break

        if linija2 == "student":
            student += 1
        elif linija2 == "standard":
            standard += 1
        elif linija2 == "kid":
            kid += 1
        ukupno_karti += 1
        broj_popunjenih_mesta += 1

        if(broj_popunjenih_mesta == broj_slobodnih_mesta_u_sali):
            break
    print(f"{naziv_filma} - {((broj_popunjenih_mesta / broj_slobodnih_mesta_u_sali) * 100):.2f}% full.")