from datetime import date

today = date.today()
print("Welcome to the Shopping Cart Program!\n")


def menu():
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print()


content = []
added_item = ""
prices = []
price = 0
removed_item = 0
menu()
action = int(input("Please enter an action: "))
while action != 5:
    if action == 1:
        added_item = input("What item would you like to add?: ")
        content.append(added_item)
        price = float(input(f"What is the price of '{added_item}'?: $"))
        prices.append(price)
        print(f"{added_item} has been added to the cart\n")
        menu()
        action = int(input("Please enter an action: "))
    elif action == 2:
        print("The contents of the shopping cart are: ")
        for i in range(len(content)):
            added_item = content[i]
            price = prices[i]
            i = i + 1
            print(f"{i}. {added_item.capitalize()} - ${price}")
        print()
        menu()
        action = int(input("Please enter an action: "))

    elif action == 3:
        removed_item = int(input("Which item would you like to remove?: "))
        removed_item -= 1
        content.pop(removed_item)
        prices.pop(removed_item)
        print("Item removed.")
        print()
        menu()
        action = int(input("Please enter an action: "))
    elif action == 4:
        total_price = 0
        for price in prices:
            total_price += price
        print("********************* YOUR CART **********************")
        for i in content:
            print(i.capitalize(), end=" ")
        print()
        print(f"The total price is : ${total_price:.2f}")
        print(f"\n~ ~ ~ Date: {today.strftime('%A, %dth of %B %Y')} ~ ~ ~")
        print("******************************************************")
        menu()
        action = int(input("Please enter an action: "))
    else:
        print("please enter a valid number")
        action = int(input("Please enter an action: "))
print("\nThank you, Good bye, hope to see you next time!!\n")
