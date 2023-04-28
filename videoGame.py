import sqlite3

#function for the user to view all available games
def viewAllGames():
    #connect to the database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    #Retrieve all the games from the database
    c.execute("SELECT * FROM videoGames")
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

