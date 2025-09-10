cart = []
def add_to_cart(item):
    cart.append(item)
def remove_from_cart(item):
    cart.remove(item)
def view_cart():
    return cart
def search_item(item):
    return item in cart
while True:
    print("\nE-commerce Cart Menu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Search for an item in cart")
    print("5. number of items in cart")
    print("6. sort the items in cart")
    print("7. clear the cart")
    print("any other key to  Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        item=input("Enter the item to add: ")
        add_to_cart(item)
        print(f"{item} added to cart.")
    elif choice == '2':
        item=input("Enter the item to remove: ")
        if search_item(item):
            remove_from_cart(item)
    elif choice == '3':
        view_cart()
    elif choice == '4':
        item=input("Enter the item to search: ")
        found=search_item(item)
        if found:
            print(f"{item} is in the cart.")
        else:
            print(f"{item} is not in the cart.")
    elif choice == '5':
        print("Number of items in cart:", len(cart))
    elif choice == '6':
        cart.sort()
        print("Cart items sorted.")
    elif choice == '7':
        cart.clear()
        print("Cart cleared.")
    else:
        break
