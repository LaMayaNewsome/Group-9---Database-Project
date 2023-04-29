import sqlite3
import os

conn = sqlite3.connect('site.db')

def createAccount():

    if os.path.exists("site.db"):
        conn = sqlite3.connect("site.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("site.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE users
            (username text, password text)''')

    username = input("Enter account username to add: ")
    password = input("Enter account password to add: ")

    c.execute("INSERT INTO users VALUES (?, ?)", [username, password])

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

        c.execute('''CREATE TABLE users
                (username text, password text)''')

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", [username, password])

    if c.fetchone() == None:
        print("Incorrct credentials")
    else:
        print("Logged in!")   


def editPayment():
    payment = input("Enter New Card Number: ")

    conn.execute("DELETE FROM users WHERE payment = ?, INSERT INTO users (payment) VALUES (?)", (payment))

def editShipping():
    shippingAddress = input("Enter New Address: ")

    conn.execute("INSERT INTO users (shippingAddress) VALUES (?)", (shippingAddress))

def logout():
    #logout = input("Enter 6 to logout.")
    pass

#test logout
logout()
print('Logged Out Successfully.')

def deleteUser():
    conn.execute("DELETE FROM user WHERE username = ?, DELETE FROM users WHERE payment = ?, DELETE FROM users WHERE shippingAddress = ?", ('current user',))

    conn.commit()
    conn.close()