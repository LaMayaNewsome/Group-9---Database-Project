import sqlite3

def inventory_editQuantity(item_Quantity):
    item_id = int(input("Enter the ID of the product (either tshirt or video game) you want change the quantity of: "))

    conn = sqlite3.connect('site.db')
    c = conn.cursor()

    # Execute an SQL UPDATE statement to update values in the database
    if item_id in range(101,103):
        c.execute("UPDATE inventory SET quantity = ?", (item_Quantity))
    
    elif item_id in range(1,3):
        c.execute("UPDATE inventory SET quantity = ?", (item_Quantity))
    
    else:
        print("Item ID Not Found, Please Try Again...")

    # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()

def add_to_cart():
    item_id = int(input("Enter the ID of the product (either tshirt or video game) you want to add to your cart: "))
    quantity = int(input("Enter the quantity you want to add to your cart: "))

    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    if item_id in range(101,103): #T-Shirt Selection
        cursor.execute('SELECT item_quantity FROM t_shirts WHERE t_shirt_id=?', (item_id))
        item_quantity = cursor.fetchone()[0]

        if item_quantity < quantity:
            print("Insufficient stock!")
        else:
            cursor.execute(
                'INSERT INTO shopping_cart (customer_id, t_shirt_id, quantity) VALUES (?, ?, ?)', (1, item_id, item_quantity))
            cursor.execute(
                'UPDATE inventory SET item_quantity=item_quantity-? WHERE t_shirt_id=?', (quantity, item_id))
            conn.commit()
            print("T-shirt added to cart successfully!")
    
    elif item_id in range(1,3): #Video Game Selection
        cursor.execute('SELECT item_quantity FROM t_shirts WHERE gameID=?', (item_id))
        item_quantity = cursor.fetchone()[0]

        if item_quantity < quantity:
            print("Insufficient stock!")
        else:
            cursor.execute(
                'INSERT INTO shopping_cart (customer_id, gameID, quantity) VALUES (?, ?, ?)', (1, item_id, quantity))
            cursor.execute(
                'UPDATE inventory SET item_quantity=item_quantity-? WHERE gameID=?', (quantity, item_id))
            conn.commit()
            print("Video Game added to cart successfully!")
    
    else:
        print("Product ID Not Found, Please Try Again! :D")
    

    conn.close()

def remove_from_cart():
    cart_id = int(
        input("Enter the ID of the item you want to remove from your cart: "))

    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM shopping_cart WHERE cart_id=?', (cart_id))
    item = cursor.fetchone()

    if item is None:
        print("Item not found in cart!")
    elif item in range(101,103):
        cursor.execute('DELETE FROM shopping_cart WHERE cart_id=?', (cart_id,))
        cursor.execute(
            'UPDATE inventory SET quantity=quantity+? WHERE t_shirt_id=?', (item[3], item[2]))
        conn.commit()
        print("Item removed from cart successfully!")
    elif item in range(1,3):
        cursor.execute('DELETE FROM shopping_cart WHERE cart_id=?', (cart_id,))
        cursor.execute(
            'UPDATE inventory SET quantity=quantity+? WHERE gameID=?', (item[3], item[2]))
        conn.commit()
        print("Item removed from cart successfully!")

    conn.close()


def main():
    while True:
        print("\nMenu:")
        print("1. Edit an item's Quantity")
        print("2. Add Item to Shopping Cart")
        print("3. Remove item from Shopping Cart")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            inventory_editQuantity()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            remove_from_cart()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
