import sqlite3
import os

def editPayment():
    cardNumber = input("Enter New Card Number: ")

    conn.execute("DELETE FROM Payment WHERE cardNumber = ?, INSERT INTO Payment (cardNumber) VALUES (?)", (cardNumber))