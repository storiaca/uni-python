'''
6. Building
Write a function that outputs on the console the room numbers in a building (in descending order) when the following conditions are met:
    • On each even floor, there are only offices
    • On each odd floor, there are only apartments
    • Each apartment is marked as follows: A{floor number}{apartment number}, apartment numbers start from 0
    • Each office is marked as follows: O{floor number}{office number}, office numbers also start from 0
    • There are always apartments on the top floor, and they are bigger than the others, that is why they have 'L' instead of 'A' in front of their number. If there is only one floor, there are only big apartments!
Two integers are read from the console – the number of floors and the number of rooms per floor. 
'''
floors = int(input())
rooms_per_floor = int(input())

for i in range(floors,0,-1):
    for j in range(0, rooms_per_floor):
        if(i == floors): # ako je poslednji sprat stampamo slovo L
            print(f"L{i}{j}", end=" ")
        else:
            # ako nije poslednji sprat, mozda je parni
            if(i % 2 == 0):
                print(f"O{i}{j}", end=" ")
            else:
                print(f"A{i}{j}", end=" ")
    print("") # prelazak u novi red
# Test with: 3, 4
# Test with: 6, 4
# Test with: 1, 4