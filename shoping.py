choice = int(input("\n1.ADD ITEM \n.2.EXIT :: "))
if choice == 2:
    print("\nEXiting...")
shopdict = {}

while choice == 1:    

    item = str(input("\nEnter item name : "))
    price = int(input("\nEnter the price of item : "))
    shopdict[item] = price
    ask = int(input("1.ADD MORE ITEM\n2.CALCULATE EXPENCE \n ::"))
    if ask == 2 :
        print("\nCalculating...\n")
        break

expense = 0
for i in shopdict:
    expense += shopdict[i]
print("Total expense is : ",expense)