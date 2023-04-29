import sqlite3
import os

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