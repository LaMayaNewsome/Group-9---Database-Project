import sqlite3

# Function to view available t-shirts


def view_tshirts():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM t_shirts')
    tshirts = cursor.fetchall()

    print("Available t-shirts:")
    for tshirt in tshirts:
        print(
            f"ID: {tshirt[0]}  Name: {tshirt[1]}  Color: {tshirt[2]}  Size: {tshirt[3]}  Quantity: {tshirt[4]}  Price: {tshirt[5]}")

    conn.close()

# Function to add a t-shirt to the shopping cart


def add_to_cart():
    tshirt_id = int(
        input("Enter the ID of the t-shirt you want to add to your cart: "))
    quantity = int(input("Enter the quantity you want to add to your cart: "))

    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT t_shirt_quantity FROM t_shirts WHERE t_shirt_id=?', (tshirt_id,))
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

# Function to remove a t-shirt from the shopping cart


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

# Main function to handle user input and call appropriate functions


def main():
    while True:
        print("\nMenu:")
        print("1. View available t-shirts")
        print("2. Add a t-shirt to your cart")
        print("3. Remove a t-shirt from your cart")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_tshirts()
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
