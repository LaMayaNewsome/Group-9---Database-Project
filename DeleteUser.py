import sqlite3

conn = sqlite3.connect('login.db')

conn.execute("DELETE FROM login WHERE username = ?", ('current user',))

conn.commit()
conn.close()