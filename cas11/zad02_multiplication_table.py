'''
2. Multiplication Table
Print on the console the multiplication table for the numbers 1 to 10 in the format
"{first multiplier} * {second multiplier} = {result}". 
'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")