import sqlite3

def cart_total(input_userCartID):
    allCosts = []

    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM shoppingCart where status = 0 and user_cartID = ?",
                   (input_userCartID,))

    allOrder = cursor.fetchall()

    for eachOrder in allOrder:
        tableDirect = eachOrder[2]
        product_id = eachOrder[3]
        quantityCount = eachOrder[4]

        if (tableDirect == "videoGames"):
            cursor.execute("Select * from videoGames where gameID = ?",(product_id,))
        else:
            cursor.execute("Select * from t_shirt where t_shirt_id = ?", (product_id, ))

        rows = cursor.fetchall()

        for row in rows:
            if (tableDirect == "videoGames"):
                cost1 = (float(row[3]) * float(quantityCount))
                allCosts.append(cost1)

            else:
                cost2 = (float(row[4]) * float(quantityCount))
                allCosts.append(cost2)

    totalCost = 0.0
    for eachCost in allCosts:
        totalCost = float(totalCost) + float(eachCost)

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    print(totalCost)
    return totalCost

def cart_checkout(input_userCartID):
    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("UPDATE shoppingCart SET status = ? WHERE user_cartID = ?", (-1, input_userCartID))

    conn.commit()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    print("Checkout Complete!")
def review_all_cart(input_userCartID):
    # Connect to the database file

    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM shoppingCart where status = 0 and user_cartID = ?",
                   (input_userCartID,))

    allOrder = cursor.fetchall()

    for eachOrder in allOrder:
        tableDirect = eachOrder[1]
        product_id = eachOrder[2]
        if (tableDirect == "Video Game"):
            cursor.execute("Select * from videoGames where gameID = ?", (product_id,))
        else:
            cursor.execute("Select * from t_shirt where t_shirt_id = ?", (product_id,))


        ItemSet = cursor.fetchall()

        for eachItem1 in ItemSet:
            if (tableDirect == "Video Game"):
                print(eachItem1[2], " - $", eachItem1[3])
            else:
                print(eachItem1[1], " - $", eachItem1[4])


    # Close the cursor and the database connection
    cursor.close()
    conn.close()

def view_past_carts(input_user_id):
    # Connect to the database file
    conn = sqlite3.connect('site.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cursor.execute("SELECT * FROM shoppingCart where status = -1 and user_cartID = ?",
                   (input_user_id,))

    allOrder = cursor.fetchall()

    for eachOrder in allOrder:
        tableDirect = eachOrder[1]
        product_id = eachOrder[2]
        if (tableDirect == "Video Game"):
            cursor.execute("Select * from videoGames where gameID = ?", (product_id,))
        else:
            cursor.execute("Select * from t_shirt where t_shirt_id = ?", (product_id,))


        ItemSet = cursor.fetchall()

        for eachItem1 in ItemSet:
            if (tableDirect == "Video Game"):
                print(eachItem1[2])
            else:
                print(eachItem1[1])


    # Close the cursor and the database connection
    cursor.close()
    conn.close()

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

def update_item_quantity(input_userCart, input_product, input_table, input_newQuantity):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    c.execute("UPDATE shoppingCart SET status = ? WHERE user_cartID = ? AND product_id = ? AND table_name = ?",
              (-1, input_userCart, input_product, input_table))

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
