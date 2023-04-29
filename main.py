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
# import user


# Function to login or create a new account
def loginMenu():
    print("\n")
    print("Welcome to the store!")
    print("Please select an option:")
    print("1. Login")
    print("2. Create Account")
    return input("Enter your choice(1-2): ")

# Handle user choice for login


def login():
    loginChoice = loginMenu()
    if loginChoice == "1":
        # prompt user to enter login credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if login credentials are valid
        if user.login(username, password):  # enter login function here
            # if login is successful, show main menu
            displayMainMenu()
        else:
            # if login is unsccessful, show error message and return to login menu
            print("Invalid login credentias. Please try again.")
            loginMenu()
    elif loginChoice == "2":
        # Prompt the user to create a new account
        username = input("Create your username: ")
        password = input("Create your password: ")

        # Create a new account with the entered credentials
        # add function to create and account here
        user.createAccount(username, password)

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
    print("3. Exit")
    return input("Please choose and option (1-3): ")

# Function for the overall logic


def mainMenu():
    while True:
        mainChoice = displayMainMenu()
        if mainChoice == "1":
            shop()
        elif mainChoice == "2":
            print("Not yet implemented")
            # accountOptions()
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
                item_id = input(
                    "Enter the ID of the t-shirt you want to add to your cart: ")
                quantity = input("Enter the quantity you want to add: ")
                inventory_Functions.add_cart_item_product(
                1, "videoGames", item_id, quantity)  # function to add item to cart
            elif choice.lower() == "n":
                mainMenu()
            else:
                print(
                    "Incorrect Option Entered. You will now be returned back to the main menu.")
                mainMenu()
            shoppingCart.add_cart_item_product(
                1, "t_shirt", "t_shirt_id", quantity)  # function to add item to cart
        elif shopChoice == "2":
            videoGame.viewAllGames()
            choice = input(
                "Would you like to add a video game to your cart? (y/n):")
            if choice.lower() == "y":
                item_id = input(
                    "Enter the ID of the video game you want to add to your cart: ")
                quantity = input("Enter the quantity you want to add: ")
                inventory_Functions.add_cart_item_product(
                1, "videoGames", item_id, quantity)  # function to add item to cart
            elif choice.lower() == "n":
                mainMenu()
            
        elif shopChoice == "3":
            shoppingCart.review_all_cart()  # function to view cart
        elif shopChoice == "4":
            shoppingCart.cart_checkout(1)  # function to checkout
        elif shopChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            # loginMenu()


# Browse t_shirts
# the user can view all the tShirts and be able to add one to their cart

# Browse videoGames
# the user can view all the videoGames and be able to add a game to their cart

# view cart
# the user should be able to view all items in their cart and remove any item they don't want

# checkout
# the user will be able to checkout and purchase all items in the cart


# Function to display Account options menu

def displayAccountMenu():
    print("Account Options:")
    print("1. Delete account")
    print("2. Edit payment information")
    print("3. Edit shipping information")
    print("4. Order history")
    print("5. Return to main menu")
    return input("Please choose an option: ")


"""
def accountOptions():
    while True:
        accountChoice = displayAccountMenu()
        if accountChoice == "1":
            # function to delete account ex. user.deleteAccount(1)
            break
        elif accountChoice == "2":
            # function to edit payment information
        elif accountChoice == "3":
            # function to edit shippping info
        elif accountChoice == "4":
            # function to view order history
        elif accountChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            displayAccountMenu()
"""


def main():
    mainMenu()


if __name__ == "__main__":
    main()
