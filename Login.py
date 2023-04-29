import sqlite3
import os

def login():   
    
    if os.path.exists("site.db"):
        conn = sqlite3.connect("site.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("site.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE accounts
                (uname text, pwd text)''')

    uname = input("Enter Username: ")
    pwd = input("Enter Password: ")

    c.execute("SELECT * FROM accounts WHERE uname = ? AND pwd = ?", [uname, pwd])

    if c.fetchone() == None:
        print("Incorrct credentials")
    else:
        print("Logged in!")