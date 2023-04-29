#Basic Login and Delete Stuff/Logout

import sqlite3

#connect to DB
conn = sqlite3.connect('login.db')

#Creat table to store login info
conn.execute('''CREATE TABLE login
            (username TEXT PK, password TEXT)''')

#Insert test data
conn.execute("INSERT INTO login (username, password) VALUES ('user1', 'password1')")
conn.execute("INSERT INTO login (username, password) VALUES ('user2', 'password2')")

#Commit changes and close connection
conn.commit()
conn.close()

#Logout/Delete login info for current user

#Connect to DB
conn.sqlite3.connect('login.db')

#Delete Login info for current user
conn.execute("DELETE FROM login WHERE username = ?", ('current_user',))

#Commit change and close connection
conn.commit()
conn.close()