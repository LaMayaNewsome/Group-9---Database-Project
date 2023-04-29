import sqlite3

# Function to view available t-shirts


def view_tshirts():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM t_shirts')
    tshirts = cursor.fetchall()

    print("Available t-shirts:")
    for tshirt in tshirts:
        print(
            f"ID: {tshirt[0]}  Name: {tshirt[1]}  Color: {tshirt[2]}  Size: {tshirt[3]}  Quantity: {tshirt[4]}  Price: {tshirt[5]}")

    conn.close()

# Main function to handle user input and call appropriate functions
