'''
2. Password
Write a program that initially reads the username and password of a user profile. Then reads the login password.
    • On entering the wrong passwords: prompt the user to enter a new password.
    • On entering the correct password: print "Welcome {username}!".
'''
username = input()
password = input()

login_pass = input()

while(password != login_pass):
    login_pass = input()

print(f"Welcome, {username}!")