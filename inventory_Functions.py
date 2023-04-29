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

def add_to_cart():
    item_id = int(input("Enter the ID of the product (either tshirt or video game) you want to add to your cart: "))
    quantity = int(input("Enter the quantity you want to add to your cart: "))

    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    if item_id
    cursor.execute('SELECT t_shirt_quantity FROM t_shirts WHERE t_shirt_id=?', (tshirt_id,))
    tshirt_quantity = cursor.fetchone()[0]

    if tshirt_quantity < quantity:
        print("Insufficient stock!")
    else:
        cursor.execute(
            'INSERT INTO shopping_cart (customer_id, t_shirt_id, quantity) VALUES (?, ?, ?)', (1, tshirt_id, quantity))
        cursor.execute(
            'UPDATE t_shirts SET t_shirt_quantity=t_shirt_quantity-? WHERE t_shirt_id=?', (quantity, tshirt_id))
        conn.commit()
        print("T-shirt added to cart successfully!")

    conn.close()

def remove_from_cart():
    cart_id = int(
        input("Enter the ID of the item you want to remove from your cart: "))

    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM shopping_cart WHERE cart_id=?', (cart_id,))
    item = cursor.fetchone()

    if item is None:
        print("Item not found in cart!")
    else:
        cursor.execute('DELETE FROM shopping_cart WHERE cart_id=?', (cart_id,))
        cursor.execute(
            'UPDATE t_shirts SET quantity=quantity+? WHERE t_shirt_id=?', (item[3], item[2]))
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
