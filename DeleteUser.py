import sqlite3

#Get DataBases figured out namewise and such so you can delete ShipAd and PayInfo along with user.

conn = sqlite3.connect('user.db')

conn.execute("DELETE FROM user WHERE username = ?, DELETE FROM user WHERE paymentinfo = ?, DELETE FROM user WHERE shippingaddress = ?", ('current user',))

conn.commit()
conn.close()