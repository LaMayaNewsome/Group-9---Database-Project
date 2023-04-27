import sqlite3

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

remove_cartItem(1, 1, "Shirt")