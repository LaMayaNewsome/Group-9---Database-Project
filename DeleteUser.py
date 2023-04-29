import sqlite3

#Get DataBases figured out namewise and such so you can delete ShipAd and PayInfo along with user.

conn = sqlite3.connect('site.db')

conn.execute("DELETE FROM user WHERE username = ?, DELETE FROM paymentInfo WHERE cardNumber = ?, DELETE FROM shippingAddress WHERE address = ?", ('current user',))

conn.commit()
conn.close()