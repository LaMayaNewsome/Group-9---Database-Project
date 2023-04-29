import sqlite3
import os

conn = sqlite3.connect('site.db')

def editPayment():
    payment = input("Enter New Card Number: ")

    conn.execute("DELETE FROM users WHERE payment = ?, INSERT INTO users (payment) VALUES (?)", (payment))