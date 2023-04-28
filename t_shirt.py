import sqlite3


class TShirts:
    def __init__(self, db_file):
        self.conn = sqlite3.connect("site.db")
        self.cur = self.conn.cursor()

    def add_to_cart(self, customer_id, t_shirt_id, quantity):
        """Add a t-shirt to the customer's shopping cart."""
        self.cur.execute("INSERT INTO shoppingCart (customer_id, t_shirt_id, quantity) VALUES (?, ?, ?)",
                         (customer_id, t_shirt_id, quantity))
        self.conn.commit()

    def remove_from_cart(self, customer_id, t_shirt_id):
        """Remove a t-shirt from the customer's shopping cart."""
        self.cur.execute("DELETE FROM shoppingCart WHERE customer_id = ? AND t_shirt_id = ?",
                         (customer_id, t_shirt_id))
        self.conn.commit()

    def view_all_t_shirts(self):
        """View all available t-shirts."""
        self.cur.execute("SELECT * FROM t_shirt")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def search_by_color(self, color):
        query = "SELECT * FROM t_shirts WHERE t_shirt_color = ?"
        result_set = self.db.execute(query, (color,))
        return result_set.fetchall()

    def search_by_size(self, size):
        query = "SELECT * FROM t_shirts WHERE t_shirt_size = ?"
        result_set = self.db.execute(query, (size,))
        return result_set.fetchall()

    def search_by_style(self, style):
        query = "SELECT * FROM t_shirts WHERE t_shirt_name LIKE ?"
        result_set = self.db.execute(query, ('%' + style + '%',))
        return result_set.fetchall()

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()
