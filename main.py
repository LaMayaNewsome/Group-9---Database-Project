from t_shirt import TShirts
2


def option1():
    print("Option 1 selected")


def option2():
    print("Option 2 selected")
    tshirts = TShirts("my_database.db")
    while True:
        print("\nMenu:")
        print("1. View available t-shirts")
        print("2. Add a t-shirt to your cart")
        print("3. Remove a t-shirt from your cart")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            tshirts.view_all_t_shirts()
        elif choice == 2:
            tshirts.add_to_cart()
        elif choice == 3:
            tshirts.remove_from_cart()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")


def option3():
    print("Option 3 selected")


def exit_program():
    print("Exiting...")
    quit()


options = {
    '1': option1,
    '2': option2,
    '3': option3,
    '4': exit_program
}

while True:
    print("Main Menu")
    print("1. Option 1")
    print("2. Purchase a T-Shirt ")
    print("3. Option 3")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice. Please try again.")
