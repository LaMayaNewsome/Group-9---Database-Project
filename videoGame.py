import sqlite3

game1 = videoGames("001", "Action-packed game with high-end graphics", "Call of Duty: Modern Warfare", 59.99, "Xbox One")

#function for the user to view all available games
def viewAllGames():
    #connect to the database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    #Retrieve all the games from the database
    c.execute("SELECT * FROM video_games")
    all_games = c.fetchall()

    #Print the details of all the games
    for game in all_games:
        print("ID: ", game[0])
        print("Name: ", game[1])
        print("Description: ", game[2])
        print("Platform: ", game[3])
        print("Cost: ", game[4])

    #Close the database connection
    conn.close()

 
#Function to add a new game to the user's cart
def addGame():
    #Connect to the database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    #Prompt the user to enter the ID of the game they want to add
    game_name = int(input("Enter the name of the game ou want to add to your cart: "))

    #Check if the game exists in the database
    c.execute("SELECT * FROM videoGames WHERE Name = '?'", (game_name))
    game = c.fetchone()

    if game is None:
        print("Game not found!")
        return
    #Prompt the user to enter the quantity of the game you want to add to their cart
    quantity = int(input("Enter the quantity of the game you want to add to your cart: "))

    #Add the game to the user's cart
    c.execute("INSERT INTO cart (game_name, quantity) VALUES (?, ?)", (game_name, quantity))

def removeGame():
    #Connect to the database 
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    #Prompt the user to enter the ID of the game they want to remove

