'''
6. Vowels Sum  
Write a program that reads text (string) entered by the user and calculates and prints the sum of the vowel values according to the table below:
'''
# moje resenje
text = input()

sum = 0

for letter in text:
    if(letter == 'a'):
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5
print(sum)

# resenje sa casa sa recnikom
text = input()
sum = 0

r = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

for letter in text:
    sum += r.get(letter, 0)
print(sum)