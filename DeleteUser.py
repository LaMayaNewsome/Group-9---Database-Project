import sqlite3

#Get DataBases figured out namewise and such so you can delete ShipAd and PayInfo along with user.

conn = sqlite3.connect('site.db')

conn.execute("DELETE FROM user WHERE username = ?, DELETE FROM users WHERE payment = ?, DELETE FROM users WHERE shippingAddress = ?", ('current user',))

conn.commit()
conn.close()