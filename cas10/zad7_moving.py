'''
7. Moving
On Jose's eighteenth birthday, he decided that he was going to move out to live in an apartment. He packed his stuff in boxes and found an ad for a suitable apartment to rent. He began moving his stuff in pieces because he couldn't carry it all at once. He has limited free space in his new apartment where he can place his stuff so that the place is suitable for living.
Write a program that calculates the free volume of Jose's apartment that remains after he moves his stuff. 
Each box is of exact size:  1m. x 1m. x 1m.
'''
slobodna_zapremina = int(input()) * int(input()) * int(input())
linija = ""

while True:
    linija = input()
    if linija == "Done":
        # radim nesto
        print(f"{slobodna_zapremina} Cubic meters left.")
        break
    linija = int(linija)
    slobodna_zapremina -= linija
    if slobodna_zapremina <= 0:
        # radim nesto
        print(f"No more free space! You need {abs(slobodna_zapremina)} Cubic meters more.")
        break

