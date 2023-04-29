import sqlite3

conn = sqlite3.connect('user.db')

def editShipping():
    shippingAddress = input("Enter New Address: ")

    conn.execute("DELETE FROM Shipping WHERE shippingAddress = ?, INSERT INTO Shipping (shippingAddress) VALUES (?)", (shippingAddress))

def editPayment():
    cardNumber = input("Enter New Card Number: ")

    conn.execute("DELETE FROM Payment WHERE cardNumber = ?, INSERT INTO Payment (cardNumber) VALUES (?)", (cardNumber))