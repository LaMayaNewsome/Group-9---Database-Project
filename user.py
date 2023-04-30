import sqlite3
import os
import main

conn = sqlite3.connect('site.db')


def createAccount():

    if os.path.exists("site.db"):
        conn = sqlite3.connect("site.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("site.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE user
            (username text, password text)''')

    username = input("Enter account username to add: ")
    password = input("Enter account password to add: ")
    shippingAddress = input("Enter Shipping Address: ")
    payment = input("Enter Card Number: ")

    c.execute("INSERT INTO user VALUES (?, ?, ?, ?)", [
              username, password, shippingAddress, payment])

    conn.commit()
    conn.close()

    print("Account added")
    main.loginMain()


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
        main.mainMenu()


def editPaymentInfo(userID):
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Retrieve current payment info
    c.execute("SELECT payment_info FROM users WHERE user_id = ?", (userID,))
    current_payment_info = c.fetchone()[0]

    print("Your current payment info is:", current_payment_info)

    # Prompt user for new payment info
    new_payment_info = input("Enter your new payment info: ")

    # Update payment info in the database
    c.execute("UPDATE users SET payment_info = ? WHERE user_id = ?",
              (new_payment_info, userID))
    conn.commit()

    print("Payment info updated successfully!")

    conn.close()


def editShipping():
    shippingAddress = input("Enter New Address: ")

    conn.execute("INSERT INTO user (shippingAddress) VALUES (?)",
                 (shippingAddress))


def logout():
    conn.close()  # Closing the connection is the logout


def deleteUser():
    conn.execute("DELETE FROM user WHERE username = ?, DELETE FROM user WHERE payment = ?, DELETE FROM user WHERE shippingAddress = ?", ('current user',))

    conn.commit()
    conn.close()
