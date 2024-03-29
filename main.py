# Methods and tools project
# LaMaya Newsome - ljn72
# Keshawn Davis - kld609
# Lucas Foley - lhf57
# Sam Hankins - sgh243
# Maxwell Lam - mvl57

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
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        # Call createAccount() with the username and password
        user.createAccount(username, password)
        print("Account created successfully. Please log in. \n")
        user.login()

    else:
        print("Invalid choice. Please try again. \n")
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


def mainMenu(username):
    while True:
        mainChoice = displayMainMenu()
        if mainChoice == "1":
            shop(username)
        elif mainChoice == "2":
            accountOptions(username)
        elif mainChoice == "3":
            print("Thank you for shopping at Walmart!")
            loginMain()
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
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Return to main menu")
    return input("Please choose an option: ")


def shop(username):
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
                displayShopMenu()
            else:
                print(
                    "Incorrect Option Entered. You will now be returned back to the shop menu.")
                displayShopMenu()

        elif shopChoice == "2":
            videoGame.viewAllGames()
            choice = input(
                "Would you like to add a video game to your cart? (y/n):")
            if choice.lower() == "y":
                inventory_Functions.add_to_cart()
            elif choice.lower() == "n":
                displayShopMenu()
            else:
                print("Incorrect Option Entered. You will now be returned back to the shop menu.")
                displayShopMenu()

        elif shopChoice == "3":

            tokenId = user.nameToID(username)
            shoppingCart.review_all_cart(tokenId)  # function to view cart
            choice = input(
                "Would you like to remove an item from your cart? (y/n):")
            if choice.lower() == "y":
                inventory_Functions.remove_from_cart(tokenId)
            elif choice.lower() == "n":
                mainMenu(username)

        elif shopChoice == "4":
            tokenId = user.nameToID(username)
            shoppingCart.cart_checkout(tokenId)  # function to checkout
        elif shopChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            loginMenu()

# view cart
# the user should be able to view all items in their cart and remove any item they don't want

# Function to display Account options menu
def displayAccountMenu():
    print("\n\nAccount Options:")
    print("1. Delete account")
    print("2. Edit payment information")
    print("3. Edit shipping information")
    print("4. Order history")
    print("5. Return to main menu")
    return input("Please choose an option: ")


def accountOptions(username):
    while True:
        accountChoice = displayAccountMenu()
        if accountChoice == "1":
            username = input("Please enter your username to delete your account:")
            user.deleteUser(username)
            loginMain()
            break
        elif accountChoice == "2":
            username = input("Please enter your username to edit payment info:")
            user.editPaymentInfo(username)
        elif accountChoice == "3":
            username = input("Please enter your username to edit shipping info:")
            user.editShipping(username)
        elif accountChoice == "4":
            print("Order History")
            tokenId = user.nameToID(username)
            shoppingCart.view_past_carts(tokenId)
        elif accountChoice == "5":
            displayMainMenu()
            break
        else:
            print("Invalid choice. Please try again.")
            displayAccountMenu()


def main():
    loginMain()


if __name__ == '__main__':
    main()
