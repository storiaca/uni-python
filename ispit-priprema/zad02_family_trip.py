'''
2. Family Trip
The Smiths family is planning their family vacation. Your task is to write a program that calculates whether their budget will be enough, knowing how many nights they have planned, what is the price per night and what percentage of the budget they have provided for additional costs You also know that if the number of nights is more than 7, the price per night is reduced by 5%. 
Input Data
Read 4 lines from the console:
    • The budget they have – a floating-point number in the range [1.00 … 10000.00]
    • The number of nights – integer in the range [0 … 1000]
    • Price per night – a floating-point number in the range [1.00 … 500.00]
    • The percentage for additional costs – integer in the range [0 … 100]
'''
budzet = float(input())
broj_noci = int(input())
cena_po_noci = float(input())
procenat_dt = int(input())

if broj_noci > 7:
    #cena po noci se redukuje(smanjuje) 100-5=95
    cena_po_noci = (95/100) * cena_po_noci

dodatni_troskovi = (procenat_dt/100) * budzet

ukupna_cena = broj_noci * cena_po_noci + dodatni_troskovi

if(ukupna_cena <= budzet):
    print(f"Smiths will be left with {(budzet-ukupna_cena):.2f} USD after vacation.")
else:
    print(f"{abs(ukupna_cena - budzet):.2f} USD needed.")