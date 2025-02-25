'''
4. Train the Trainers
The "Train the trainers" course is coming to an end and the final evaluation is approaching. Your task is to help the jury that will evaluate the presentations by writing a program in which to calculate the average grade of each of the student’s presentations, and finally - the average grade of all of them. 
'''
n = int(input())
linija = ""
ukupna_ocena = 0.00
ukupni_broj_ocena = 0
while True:
    linija = input()
    if linija == "Finish":
        break
    naziv_prezentacije = linija
    suma_ocena = 0.0
    for i in range(n): # tipicna petlja koja se ponavlja n puta
        suma_ocena += float(input())
    ukupni_broj_ocena += n
    ukupna_ocena += suma_ocena
    print(f"{naziv_prezentacije} - {((suma_ocena/n)):.2f}.")

print(f"Student's final assessment is {(ukupna_ocena/ukupni_broj_ocena):.2f}.")