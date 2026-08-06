# Create a shopping cart using a list.
# Perform:
# •	Add item 
# •	Remove item 
# •	Search item 
# •	Display cart 
# •	Count total items

shopping_cart = []
choice = ""

while(choice<='5'):

    print("1. Add an item \n2. Remove an item\n3. Search for an item \n4. Display cart\n5. Count total items\n")
    choice = input("Enter a choice: ")

    if choice == '1':
        item = input("Enter an item: ")
        shopping_cart.append(item)

    elif choice == '2':
        if len(shopping_cart)>0:
            item = input("Enter item to be removed: ")
            shopping_cart.remove(item)

    elif choice == '3':
        item = input("Enter item to search: ")
        if item in shopping_cart:
            position = shopping_cart.index(item) + 1
            print("Item found at position:", position)
        else:
            print("Item not found.")

    elif choice == '4':
        print(f"The shopping cart is: {shopping_cart}")

    elif choice == '5':
        length = len(shopping_cart)
        print("The length of the shopping cart is",length)

    else:
        print("Invalid Input")