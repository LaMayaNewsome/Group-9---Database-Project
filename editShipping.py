import sqlite3
import os

conn = sqlite3.connect('site.db')

def editShipping():
    shippingAddress = input("Enter New Address: ")

    conn.execute("INSERT INTO users (shippingAddress) VALUES (?)", (shippingAddress))


#"DELETE FROM Shipping WHERE shippingAddress = ?,