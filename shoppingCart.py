import sqlite3
def review_all_cart():
    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM shoppingCart")

    # Fetch all rows of the result set and store them in a list of tuples
    rows = cursor.fetchall()

    for r in rows:
        print(r[0])

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Convert the list of tuples into a list of lists
    list_of_lists = [list(row) for row in rows]

    # Print the list of lists
    print(list_of_lists)

def view_past_carts(input_user_id):
    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM shoppingCart where status = -1 and user_cartID = ?", (input_user_id,))

    # Fetch all rows of the result set and store them in a list of tuples
    rows = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Convert the list of tuples into a list of lists
    list_of_lists = [list(row) for row in rows]

    # Print the list of lists
    print(list_of_lists)

view_past_carts(1)

def add_cart_item_product(input_userCart, input_table, input_product, input_quantity):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Define the data to be added
    data = (input_userCart, input_table, input_product, input_quantity)

    # Execute an SQL INSERT statement to add data to the database
    c.execute("INSERT INTO shoppingCart (user_cartID, table_name, product_id, quantity) VALUES (?, ?, ?, ?)", data)

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def update_item_quantity(input_userCart, input_product, input_table, input_newQuantity):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    c.execute("UPDATE shoppingCart SET quantity = ? WHERE user_cartID = ? AND product_id = ? AND table_name = ?",
              (input_newQuantity, input_userCart, input_product, input_table))

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def remove_cartItem(input_userCart, input_product, input_table):
# Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL DELETE statement to remove data from the database
    c.execute("DELETE FROM shoppingCart WHERE user_cartID = ? AND product_id = ? AND table_name = ?", (input_userCart, input_product, input_table))

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()
