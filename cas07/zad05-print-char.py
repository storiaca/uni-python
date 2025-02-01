'''
5. Character Sequence
Write a program that receives text (string) and prints each character of the string on a separate line.
'''
characters = input()

for i in range(0, len(characters)):
    print(characters[i])

# drugi nacin
for slovo in characters:
    print(slovo)