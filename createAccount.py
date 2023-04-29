import sqlite3
import os

def createAccount():

    if os.path.exists("site.db"):
        conn = sqlite3.connect("site.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("site.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE accounts
            (uname text, pwd text)''')

    uname = input("Enter account username to add: ")
    pwd = input("Enter account password to add: ")

    c.execute("INSERT INTO accounts VALUES (?, ?)", [uname, pwd])

    conn.commit()
    conn.close()

    print("Account added")

