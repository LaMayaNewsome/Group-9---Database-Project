import sqlite3
import os
import main

conn = sqlite3.connect('site.db')

def nameToID(username):
    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM user where username = ?", (username,))

    names = cursor.fetchall()

    for name in names:
        return name[2]

def register(username, password):
    # Check if the user_id column exists in the users table
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(user)")
    columns = cur.fetchall()
    userID_exists = False
    for column in columns:
        if column[1] == "userID":
            userID_exists = True
            break
    if not userID_exists:
        # Create the user_id column if it does not exist
        cur.execute("ALTER TABLE user ADD COLUMN userID INTEGER PRIMARY KEY")
        conn.commit()
    # Get the highest existing user ID from the database
    cur.execute("SELECT MAX(userID) FROM user")
    max_userID = cur.fetchone()[0]
    if max_userID is None:
        max_userID = 0
    # Generate a new user ID by adding 1 to the highest existing user ID
    userID = max_userID + 1
    cur.execute("INSERT INTO user (userID, username, password) VALUES (?, ?, ?)",
                (userID, username, password))
    conn.commit()
    return userID  # Return the new user ID


def createAccount(username, password):
    # Register the new user and get the user ID
    userID = register(username, password)
    # Insert the user's details into the users table
    cur = conn.cursor()
    cur.execute("INSERT INTO user (userID, username, password) VALUES (?, ?, ?)",
                (userID, username, password))
    conn.commit()


def login():

    if os.path.exists("site.db"):
        conn = sqlite3.connect("site.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("site.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE user
                (username text, password text)''')

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    c.execute("SELECT * FROM user WHERE username = ? AND password = ?",
              [username, password])

    if c.fetchone() == None:
        print("Incorrct credentials")
        main.mainMenu()
    else:
        print("Logged in!")
        main.mainMenu(username)

def editPaymentInfo(username):
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Retrieve current payment info
    c.execute("SELECT payment FROM user WHERE username = ?", (username,))
    result = c.fetchone()
    if result is None:
        print("User not found.")
        conn.close()
        return

    current_payment_info = result[0]
    print("Your current payment info is:", current_payment_info)

    # Prompt user for new payment info
    new_payment_info = input("Enter your new payment info: ")

    # Update payment info in the database
    c.execute("UPDATE user SET payment = ? WHERE username = ?", (new_payment_info, username))
    conn.commit()

    print("Payment info updated successfully!")

    conn.close()



def editShipping(username):
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Retrieve current payment info
    c.execute("SELECT shippingAddress FROM user WHERE username = ?", (username,))
    result = c.fetchone()
    if result is None:
        print("User not found.")
        conn.close()
        return

    current_shipping_info = result[0]
    print("Your current shipping info is:", current_shipping_info)

    # Prompt user for new payment info
    new_shipping_info = input("Enter your new shipping info: ")

    # Update payment info in the database
    c.execute("UPDATE user SET shippingAddress = ? WHERE username = ?", (new_shipping_info, username))
    conn.commit()

    print("Shipping info updated successfully!")

    conn.close()
    
def deleteUser(username):
    conn.execute("DELETE FROM user WHERE username = ?", (username,))
    token = nameToID(username)
    conn.execute("UPDATE shoppingCart SET status = -1 WHERE user_cartID = ? ", (token,))
    #Status = -1 means removed for Order History purposes
    conn.commit()
    conn.close()

