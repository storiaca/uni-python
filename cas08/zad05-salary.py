'''
5. Salary 
A company boss notices that more and more employees are spending time on sites that distract them.  
To prevent this, he introduces surprise checks on his employees' opened browser tabs. 
According to the opened tab site, the following fines are applied:
    • "Facebook" -> 150 USD
    • "Instagram" -> 100 USD
    • "Reddit" -> 50 USD
'''
number_tabs = int(input())
salary = int(input())

for i in range(number_tabs): # number_tabs puta citamo nazive sajtova i redujkujemo platu
    tab = input()
    if(tab == "Facebook"):
        salary -= 150
    elif(tab == "Instagram"):
        salary -= 100
    elif(tab == 'Reddit'):
        salary -= 50

if(salary <= 0):
    print("You have lost your salary.")
else:
    print(salary)