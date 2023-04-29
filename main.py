<<<<<<< HEAD
#Methods and tools project
#LaMaya Newsome - ljn72
#Keshawn Davis - 
#Lucas Foley
#Sam Hankins
#Maxwell Lam - mvl57
=======
# Methods and tools project
# LaMaya Newsome - ljn72
# Keshawn Davis - kld609
# Lucas Foley - lhf57
# Sam Hankins
# Maxwell
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37

import videoGame
import shoppingCart
import inventory_Functions
import Tshirt
<<<<<<< HEAD
#import user
=======
# import user
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37


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
<<<<<<< HEAD
        #prompt user to enter login credentials
        print("\n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        """
        #Check if login credentials are valid
        if user.login(username, password):   #enter login function here
            #if login is successful, show main menu
            mainMenu()
=======
        # prompt user to enter login credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if login credentials are valid
        if user.login(username, password):  # enter login function here
            # if login is successful, show main menu
            displayMainMenu()
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
        else:
            # if login is unsccessful, show error message and return to login menu
            print("Invalid login credentias. Please try again.")
            loginMenu()
        """
        mainMenu()

    elif loginChoice == "2":
<<<<<<< HEAD
        #Prompt the user to create a new account
        print("\n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        """
        #Create a new account with the entered credentials
        user.createAccount(username, password) #add function to create and account here
        
        #Show success message and return to login menu
=======
        # Prompt the user to create a new account
        username = input("Create your username: ")
        password = input("Create your password: ")

        # Create a new account with the entered credentials
        user.createAccount(username, password)

        # Show success message and return to login menu
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
        print("Account created successfully. Please log in.")
        
        loginMenu()
    else:
        print("Invalid choice. Please try again.")
        loginMenu()
        """

        loginMenu()


# Function to display the main menu
def displayMainMenu():
    print("\n")
    print("Welcome to our e-commerce store!")
    print("1. Shop")
    print("2. Account options")
    print("3. Exit")
    return input("Please choose and option (1-3): ")

<<<<<<< HEAD
#Function for the overall logic
=======
# Function for the overall logic
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
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
                shoppingCart.add_cart_item_product(
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
                shoppingCart.add_cart_item_product(
                1, "videoGames", item_id, quantity)  # function to add item to cart
            elif choice.lower() == "n":
                mainMenu()
            
        elif shopChoice == "3":
            shoppingCart.review_all_cart()  # function to view cart
<<<<<<< HEAD
            
        elif shopChoice == "4":
            print("Checkout :)")
            #function to checkout shoppingCart.checkout(1)
=======
        elif shopChoice == "4":
            shoppingCart.cart_checkout(1)  # function to checkout
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
        elif shopChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            # loginMenu()

# view cart
# the user should be able to view all items in their cart and remove any item they don't want

# checkout
# the user will be able to checkout and purchase all items in the cart


<<<<<<< HEAD


#Function to display Account options menu
=======
# Function to display Account options menu
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
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
<<<<<<< HEAD
            print("Edit payment information")
            #function to edit payment information
        elif accountChoice == "3":
            print("Edit shipping information")
            #function to edit shippping info
        elif accountChoice == "4":
            print("order history")
            #function to view order history
=======
            # function to edit payment information
        elif accountChoice == "3":
            # function to edit shippping info
        elif accountChoice == "4":
            # function to view order history
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
        elif accountChoice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            displayAccountMenu()
<<<<<<< HEAD
        
def main():
    login()


if __name__ == '__main__':
    main()
=======
"""


def main():
    mainMenu()


if __name__ == "__main__":
    main()
>>>>>>> 4cf1c64a062a1889a61a2f34c31e0dd409e38b37
