import sqlite3

def inventory_Add(item_ID, item_Name, item_Category, item_Quantity):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db') #change to inventory.db if I need to make a data base for it?
    c = conn.cursor()

    # Define the data to be added
    data = (item_ID, item_Name, item_Category, item_Quantity)

    # Execute an SQL INSERT statement to add data to the database
    c.execute("INSERT INTO inventory (item_ID, item_Name, item_Category, item_Quantity) VALUES (?, ?, ?, ?)", data)

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def inventory_Remove(item_Name):
# Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL DELETE statement to remove data from the database
    c.execute("DELETE FROM inventory WHERE item_Name = ?", (item_Name))

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def inventory_editQuantity(item_Quantity):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    c.execute("UPDATE inventory SET quantity = ?", (item_Quantity))

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def inventory_editName(item_Name):
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    c.execute("UPDATE inventory SET name = ?", (item_Name))

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def inventory_List():
    # Connect to the SQLite database
    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    c.execute("SELECT item_Name, item_Category, item_Quantity FROM inventory")

    rows = c.fetchall()

    for row in rows:
        item_Name, item_Category, item_Quantity = row
        print(f"Item: {item_Name} - Category: {item_Category} - Quantity: {item_Quantity}")

    # Close the database connection
    conn.close()
