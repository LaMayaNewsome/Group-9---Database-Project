import sqlite3

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

    # Main function to handle user input and call appropriate functions


def main():
    while True:
        print("\nMenu:")
        print("1. View available items")
        print("2. Edit an item's quantity in inventory")
        print("3. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            inventory_List()
        elif choice == 2:
            inventory_editQuantity()
        elif choice == 3:
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
