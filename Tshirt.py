import sqlite3

# Function to view available t-shirts


def view_all_tshirts():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Retrieve all the t-shirts and their quantities from the database
    c.execute("SELECT t_shirts.*, inventory.quantity FROM t_shirts INNER JOIN inventory ON t_shirts.t_shirt_id = inventory.t_shirt_id")
    all_tshirts = c.fetchall()

    # Print the details of all the t-shirts
    for tshirt in all_tshirts:
        print("\n")
        print("ID: ", tshirt[0])
        print("Name: ", tshirt[1])
        print("Color: ", tshirt[2])
        print("Size: ", tshirt[3])
        print("Price: ", tshirt[4])
        print("Quantity: ", tshirt[5])

    # Close the database connection
    conn.close()
