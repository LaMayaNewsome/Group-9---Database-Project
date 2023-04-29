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

# Main function to handle user input and call appropriate functions

def main():
    while True:
        print("\nMenu:")
        print("1. View available t-shirts")
        print("2. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_tshirts()
        elif choice == 2:
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
