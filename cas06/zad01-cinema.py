'''
1. Cinema
In a cinema, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of screenings with tickets at different prices:
    • Premiere – premiere screening, at a price of 12.00 USD.
    • Normal – standard screening, at a price of 7.50 USD.
    • Discount – screening for children, and students at a reduced price of 5.00 USD.
Write a program that reads the type of projection (string), a number of rows, and a number of columns in the hall (integers) entered by the user and calculates the total ticket revenue for a full hall. Print the result in the format as in the examples below, 2 characters after the decimal point.
'''
type_projection = input()
rows = int(input())
columns = int(input())
income = 0

if(type_projection == "Premiere"):
   income = (rows * columns) * 12.00
elif (type_projection == "Normal"):
    income = (rows * columns) * 7.5
elif(type_projection == "Discount"):
    income = (rows * columns) * 5.00
print(f"{income:.2f} USD")

# drugi nacin
tip_projekcije = input()
redovi = int(input()) 
kolone = int(input())

broj_mesta = redovi * kolone
cena_sedista = 0.00

if tip_projekcije == "Premiere":
    cena_sedista = 12.00 
elif tip_projekcije == "Normal":
    
    cena_sedista = 7.50
elif tip_projekcije == "Discount":
    cena_sedista = 5.00

print(f"{broj_mesta * cena_sedista:.2f} USD")