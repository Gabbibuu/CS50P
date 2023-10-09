due = 50
valid_coins = [25, 10, 5]
while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    if coin in valid_coins:
        due -= coin
print("Change Owed:", abs(due))