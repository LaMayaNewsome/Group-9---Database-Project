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

    c.execute("INSERT INTO user VALUES (?, ?)", [username, password])

    conn.commit()
    conn.close()

    print("Account added")


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
        main.displayMainMenu()
        print("Logged in!")


def editPayment():
    payment = input("Enter New Card Number: ")

    conn.execute(
        "DELETE FROM user WHERE payment = ?, INSERT INTO user (payment) VALUES (?)", (payment))


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
