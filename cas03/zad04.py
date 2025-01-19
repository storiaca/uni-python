'''
4. Password Guess
Write a program that reads a password (string) entered by the user and checks if the entered password matches the phrase "s3cr3t!P@ssw0rd". In case of coincidence, display "Welcome". In case of discrepancy, display "Wrong password!".
'''
pass_name = input()

if pass_name == 's3cr3t!P@ssw0rd':
    print('Welcome')
else:
    print('Wrong password!')