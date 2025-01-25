coke = int(50)
change = int(0)

while coke > 0:
    print("Amount Due:", coke)
    payment = int(input("Insert Coin:").strip())
    if payment == 50 or payment == 25 or payment == 10 or payment == 5 or payment == 0:
        coke = coke - payment
        if coke < 0:
            change = abs(coke)
            print("Change Owed:", change)
        print("Change Owed:", change)
    elif payment > 50 or payment < 0:
        break