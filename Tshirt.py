import sqlite3

# Function to view available t-shirts

def view_all_tshirts():
    # Connect to the database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Retrieve all the t-shirts and their quantities from the database
    c.execute("SELECT * FROM t_shirt")
    all_tshirts = c.fetchall()

    # Print the details of all the t-shirts
    for tshirt in all_tshirts:
        print("ID: ", tshirt[0])
        print("Name: ", tshirt[1])
        print("Color: ", tshirt[2])
        print("Size: ", tshirt[3])
        print("Cost: ", tshirt[4])
        print("\n")