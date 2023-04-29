import sqlite3

#Get DataBases figured out namewise and such so you can delete ShipAd and PayInfo along with user.

conn = sqlite3.connect('login.db')

conn.execute("DELETE FROM login WHERE username = ?", ('current user',))

conn.commit()
conn.close()