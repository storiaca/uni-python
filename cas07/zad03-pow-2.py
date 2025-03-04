'''
3. Even Powers of 2 
Write a program that receives a number n and prints the even powers of 2 ≤ 2n: 20, 22, 24, 26, …, 2n. 
'''

# moje resenje
n = int(input())

n = int(input())

broj = 1
for num in range(0, n+1, 2):
    broj = pow(2, num)
    print(broj)

# resenje sa casa
n = int(input()) 

for i in range(0, n+1, 2):
    print(2**i) # 2^i is not the same as 2**i, it is the XOR operator, which is not what we want here. We should use 2**i instead.

# ako zelimo da budemo sigurni da broj u range, mozemo da stavimo n+2, ili plus korak
# for i in range(start, poslednji koji zelim + korak, korak):
# ovo je najbolje resenje za for, jer je najispravnije, ali moze da se koristi i range(0, n+1, 2) za ovaj primer