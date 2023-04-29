import sqlite3
import os

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

