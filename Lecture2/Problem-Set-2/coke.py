
due = 50

while due > 0:
    print("Amount Due: ", due)

    amount = int(input("Insert Coin: "))

    if amount == 25 or amount == 10 or amount == 5:
        due = due - amount
        if due <= 0:
            due = due * -1
            print("Change Owed:", due)
            break