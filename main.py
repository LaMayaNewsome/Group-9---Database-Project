# Methods and tools project
# LaMaya Newsome - ljn72
# Keshawn Davis - kld609
# Lucas Foley - lhf57
# Sam Hankins
# Maxwell

import videoGame
import shoppingCart
import inventory_Functions
import Tshirt
import user
import turtle


# Function to login or create a new account
def loginMenu():
    print("\n")
    print("Welcome to the store!")
    print("Please select an option:")
    print("1. Login")
    print("2. Create Account")
    return input("Enter your choice(1-2): ")

# Handle user choice for login


def loginMain():
    loginChoice = loginMenu()
    if loginChoice == "1":
        user.login()

    elif loginChoice == "2":
        user.createAccount()

        # Show success message and return to login menu
        print("Account created successfully. Please log in.")
        loginMenu()
    else:
        print("Invalid choice. Please try again.")
        loginMenu()

# Function to display the main menu


def displayMainMenu():
    print("\n")
    print("Welcome to our e-commerce store!")
    print("1. Shop")
    print("2. Account options")
    print("3. Logout")
    return input("Please choose and option (1-3): ")

# Function for the overall logic


def mainMenu():
    while True:
        mainChoice = displayMainMenu()
        if mainChoice == "1":
            shop()
        elif mainChoice == "2":
            accountOptions()
        elif mainChoice == "3":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
            displayMainMenu()


# Function to display Shop menu
def displayShopMenu():
    print("\n")
    print("Shop Options:")
    print("1. Browse t-shirts")
    print("2. Browse video games")
    print("3. View cart")
    print("4. Checkout")
    print("5. Return to main menu")
    return input("Please choose an option: ")


def shop():
    while True:
        shopChoice = displayShopMenu()
        if shopChoice == "1":
            Tshirt.view_all_tshirts()  # function to view tshirts
            choice = input(
                "Would you like to add a t-shirt to your cart? (y/n):")
            if choice.lower() == "y":
               
                # function to add item to cart
                inventory_Functions.add_to_cart()
            elif choice.lower() == "n":
                mainMenu()
            else:
                print(
                    "Incorrect Option Entered. You will now be returned back to the main menu.")
                mainMenu()

        elif shopChoice == "2":
            videoGame.viewAllGames()
            choice = input(
                "Would you like to add a video game to your cart? (y/n):")
            if choice.lower() == "y":
                inventory_Functions.add_to_cart()
            elif choice.lower() == "n":
                mainMenu()

        elif shopChoice == "3":
            shoppingCart.review_all_cart()  # function to view cart
            choice = input(
                "Would you like to remove an item from your cart? (y/n):")
            if choice.lower() == "y":
                inventory_Functions.remove_from_cart()
            elif choice.lower() == "n":
                mainMenu()

        elif shopChoice == "4":
            shoppingCart.cart_checkout(1)  # function to checkout
        elif shopChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            loginMenu()

# view cart
# the user should be able to view all items in their cart and remove any item they don't want

# checkout
# the user will be able to checkout and purchase all items in the cart


# Function to display Account options menu
# Function to display Account options menu
def displayAccountMenu():
    print("Account Options:")
    print("1. Delete account")
    print("2. Edit payment information")
    print("3. Edit shipping information")
    print("4. Order history")
    print("5. Return to main menu")
    return input("Please choose an option: ")


def accountOptions():
    while True:
        accountChoice = displayAccountMenu()
        if accountChoice == "1":
            user.deleteUser(1)
            break
        elif accountChoice == "2":
            # print("Edit payment information")
            user.editPayment(2)
        elif accountChoice == "3":
            # print("Edit shipping information")
            user.editShipping(3)
        elif accountChoice == "4":
            print("order history")
        elif accountChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            displayAccountMenu()


def main():
    loginMain()


if __name__ == '__main__':
    main()
