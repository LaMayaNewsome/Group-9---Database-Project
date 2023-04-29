#Basic Login and Delete Stuff/Logout

import sqlite3

#connect to DB
conn = sqlite3.connect('login.db')

#Create table to store login info
conn.execute('''CREATE TABLE login
            (username TEXT PRIMARY KEY, password TEXT)''')

#Insert test data
conn.execute("INSERT INTO login (username, password) VALUES ('user1', 'password1')")
conn.execute("INSERT INTO login (username, password) VALUES ('user2', 'password2')")

#Commit changes and close connection
conn.commit()
conn.close()

def login(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

def logout():
    #perform logout actions here
    pass

if login('user1', 'password1'):
    print('Login successful!')
else:
    print('Login Failed.')

#test logout
logout()
print('Logged Out Successfully.')