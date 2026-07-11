all_groceries =  {
    "maggie" : 10,
    "biscuit" : 20,
    "shampoo" : 30
}

def Add():
    print("Current Stock")
    view()

    item = int(input("\n1.MAGGIEE\n2.BISCUIT\n3.SHAMPOO\nEnter the item : "))
    if item == 1:
        items = "maggie"
        pre_stock = all_groceries[items]
        add_stock = int(input("Ennter the stock : "))
        for i in all_groceries:
            if i == items:
                all_groceries[items] = add_stock + pre_stock
    if item == 2:
        items = "biscuit"
        pre_stock = all_groceries[items]
        add_stock = int(input("Ennter the stock : "))
        for i in all_groceries:
            if i == items:
                all_groceries[items] = add_stock + pre_stock
    if item == 3:
        items = "shampoo"
        pre_stock = all_groceries[items]
        add_stock = int(input("Ennter the stock : "))
        for i in all_groceries:
            if i == items:
                all_groceries[items] = add_stock + pre_stock

    else: print("Item is not available")

    print("Updated stock is :")
    view()

def view():
    for items in all_groceries:
        print(items , ":" , all_groceries[items])

def sell():
    print("\n\ncurrent stock \n")
    view()

    item = int(input("1.MAGGIE\n2.BISCUIT\n3.SHAMPOO\nENTER THE ITEM : "))
    if item == 1:
        items = "maggie"
    if item == 2:
        items = "biscuit"
    if item == 3:
        items = "shampoo"

    if 1 < item > 4:
        print("INVALID INPUT!")
        exit()
    count = int(input("How much? :"))
    updated_count = all_groceries[items] - count
    if items in all_groceries:
        all_groceries.update({items: updated_count})
    print("UPDATED STOCK : ")
    view()

while True:
    try:
        choice = int(input("1.SELL\n2.VIEW STOCK\n3.ADD STOCK\n4.EXIT\n.ENTER OPERATION >>>"))

        if choice == 1:
            sell()
        if choice == 2:
            view()
        if choice ==3:
            Add()
        if choice == 4:
            break
        if 1 < choice > 4:
            print("INVALID INPUT!")
    except ValueError:
        print("Invalid input")
print("Exiting...")