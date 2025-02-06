'''
Vezba
'''
# Print inverted triangle of stars
num_rows = int(input("Enter the number of rows: "))

for i in range(num_rows, 0, -1):
    print("*" * i)