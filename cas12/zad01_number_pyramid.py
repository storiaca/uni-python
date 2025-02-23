'''
1. Number Pyramid
Write a function that receives an integer n, entered by the user, and prints a pyramid of numbers as in the examples. 
'''
num = int(input())
curr = 1
is_curr_bigger_than_num = False

for i in range(1, num + 1):
    for j in range(1, i + 1):
        if curr > num:
            is_curr_bigger_than_num = True
            break
        print(str(curr) + ' ', end='')
        curr += 1
    if is_curr_bigger_than_num:
        break
    print()      
# resenje sa casa

n = int(input())
trenutni_broj = 0

un_petlja_prekinuta = False
for i in range(1, n+1): # redovi su 1,2,3 ...n
    for j in range(1, i+1): # imamo i brojeva u tom redu
        trenutni_broj += 1
        if(trenutni_broj > n):
            un_petlja_prekinuta = True
            break
        print(f"{trenutni_broj}", end=" ")
    print("")
    if un_petlja_prekinuta:
        break

# link za efikasniji kod
# https://chatgpt.com/share/67bb3310-6730-8012-b2a8-a6125e7ff0f8

num = int(input())
curr = 1

i = 1
while curr <= num:
    for _ in range(i):
        if curr > num:
            break
        print(curr, end=' ')
        curr += 1
    print()
    i += 1