import sqlite3

conn = sqlite3.connect('site.db')

def editShipping():
    shippingAddress = input("Enter New Address: ")

    conn.execute("DELETE FROM Shipping WHERE shippingAddress = ?, INSERT INTO Shipping (shippingAddress) VALUES (?)", (shippingAddress))
