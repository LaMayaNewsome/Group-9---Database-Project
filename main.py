import sqlite3


def view_tshirts():
    # Connect to the SQLite database
    conn = sqlite3.connect('Tshirts-group.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to retrieve all rows from the t_shirts table
    cur.execute('SELECT * FROM t_shirts')

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    print("Here are all the t-shirts in the inventory:")
    for row in rows:
        print(
            f"Name: {row[1]}, Price: {row[2]}, Size: {row[3]}, Color: {row[4]}, Style: {row[5]}, Iventory: {row[6]}")

    # Close the cursor and database connection
    cur.close()
    conn.close()


def add_to_cart():
    # Connect to the SQLite database
    conn = sqlite3.connect('Tshirts-group.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to retrieve all rows from the t_shirts table
    cur.execute('SELECT * FROM t_shirts')

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows with a numbered list for user selection
    print("Select a shirt to add to your cart:")
    for i, row in enumerate(rows):
        print(
            f"{i+1}. Name: {row[1]}, Price: {row[2]}, Size: {row[3]}, Color: {row[4]}, Style: {row[5]}, Inventory: {row[6]}")

    # Get the user's choice
    choice = int(
        input("Enter the number of the shirt you want to add to your cart: "))

    # Get the selected shirt's details
    selected_shirt = rows[choice-1]

    # Check if the inventory of the selected shirt is greater than 0
    if selected_shirt[6] > 0:
        # Decrement the inventory of the selected shirt by 1
        cur.execute(
            f"UPDATE t_shirts SET inventory = {selected_shirt[6]-1} WHERE id = {selected_shirt[0]}")
        conn.commit()

        # Display a message to confirm the shirt has been added to the cart
        print(f"Added {selected_shirt[1]} to your cart! \n")

    else:
        # Display a message if the inventory of the selected shirt is 0
        print("Sorry, this shirt is out of stock.")

    # Close the cursor and database connection
    cur.close()
    conn.close()


def remove_from_cart():
    # Connect to the SQLite database
    conn = sqlite3.connect('Tshirts-group.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to retrieve the last added shirt from the t_shirts table
    cur.execute('SELECT * FROM t_shirts ORDER BY id DESC LIMIT 1')

    # Fetch the last added shirt
    last_added_shirt = cur.fetchone()

    # Ask the user if they want to remove the last added shirt from their cart
    user_input = input(
        f"Do you want to remove {last_added_shirt[1]} from your cart? (y/n) \n")

    if user_input.lower() == 'y':
        # Increment the inventory of the last added shirt by 1
        cur.execute(
            f"UPDATE t_shirts SET inventory = {last_added_shirt[6]+1} WHERE id = {last_added_shirt[0]}")
        conn.commit()

        # Display a message to confirm the shirt has been removed from the cart
        print(f"Removed {last_added_shirt[1]} from your cart.")
    else:
        # Display a message that the shirt has not been removed from the cart
        print(f"{last_added_shirt[1]} has not been removed from your cart.")

    # Close the cursor and database connection
    cur.close()
    conn.close()


user_input = input(
    f"Would you like to view all the shirts in the inventory? (y/n) ")
if user_input.lower() == 'y':
    view_tshirts()
    u_input = input(f"Would you like to add shirt to your cart? (y/n) ")
    if u_input.lower() == 'y':
        add_to_cart()
