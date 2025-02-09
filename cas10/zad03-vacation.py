'''
3. Vacation
Jessie has decided to raise money for a vacation and wants you to help her find out if she will be able to collect the required amount. She saves or spends some of her money every day. If she wants to spend more than her available money, she will spend everything she has and will be left with 0 USD.
'''
money_for_vacation = float(input())
owned_money = float(input())

total_days = 0
days_spend = 0

while owned_money < money_for_vacation and days_spend < 5:
    command = input()
    money = float(input())
    total_days += 1
    if command == 'save':
        # dodaj pare i vrate dane za trosenje na nulu
        owned_money = owned_money + money
        days_spend = 0
    elif command == 'spend':
        # oduzmi pare i povecaj dane trosenja
        owned_money -= money
        days_spend += 1
        if owned_money < 0:
            owned_money = 0
if days_spend == 5:
    print(f"You can't save the money.")
    print(total_days)
if owned_money >= money_for_vacation:
    print(f"You saved the money for {total_days} days.")
