import random
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import mysql.connector

class ZodiacDatabase:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.create_database(host, user, password, database)
        self.create_table()

    def create_database(self, host, user, password, database):
        try:
            print(f"Connecting to MySQL server ({host}) to create or connect to the database.")
            self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
            print(f"Connected to MySQL server.")

            cursor = self.mydb.cursor(buffered=True)
    

            # Check if the database exists
            cursor.execute("SHOW DATABASES LIKE %s", (database,))
            result = cursor.fetchone()

            if not result:
                # Create the database if it doesn't exist
                print(f"Creating database '{database}'.")
                cursor.execute(f"CREATE DATABASE {database}")
                print(f"Database '{database}' created.")
            else:
                print(f"Database '{database}' already exists.")

            # Switch to the specified database
            cursor.execute(f"USE {database}")
            print(f"Using database '{database}'.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Failed to create or connect to the database.")

    def create_table(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS horoscope (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_name VARCHAR(255),
                        zodiac_sign VARCHAR(25),
                        horoscope TEXT,
                        lucky_number INT,
                        lucky_color VARCHAR(25),
                        compatibility TEXT
                    )
                """)
            self.mydb.commit()
            print("Table 'horoscope' created or already exists.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Failed to create the table.")

    def insert_data(self, user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility):
        try:
            with self.mydb.cursor() as cursor:
                sql = "INSERT INTO horoscope (user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility)
                cursor.execute(sql, val)
            self.mydb.commit()
            print("Data successfully saved to the database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Failed to save data to the database.")

    def delete_latest_entries(self, num_entries):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("SELECT id FROM horoscope ORDER BY id DESC LIMIT %s", (num_entries,))
                ids_to_delete = [entry[0] for entry in cursor.fetchall()]
                if ids_to_delete:
                    placeholders = ', '.join(['%s'] * len(ids_to_delete))
                    delete_sql = f"DELETE FROM horoscope WHERE id IN ({placeholders})"
                    cursor.execute(delete_sql, tuple(ids_to_delete))
                    self.mydb.commit()
                    print(f"Deleted {len(ids_to_delete)} latest entries.")
                else:
                    print("No entries to delete.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Failed to delete entries from the database.")

    def update_entry(self, entry_id, user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility):
        try:
            with self.mydb.cursor() as cursor:
                sql = "UPDATE horoscope SET user_name=%s, zodiac_sign=%s, horoscope=%s, lucky_number=%s, lucky_color=%s, compatibility=%s WHERE id=%s"
                val = (user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility, entry_id)
                cursor.execute(sql, val)
            self.mydb.commit()
            print(f"Entry {entry_id} updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Failed to update entry {entry_id}.")

    def get_all_entries(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("SELECT * FROM horoscope")
                entries = cursor.fetchall()
                return entries
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def delete_entry(self, entry_id):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("DELETE FROM horoscope WHERE id=%s", (entry_id,))
                self.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Failed to delete entry with ID {entry_id}.")
class ZodiacApp:
    
    def __init__(self, root, database):
        self.root = root
        self.database = database
        self.is_admin = False  
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Your Name:").grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, pady=5, padx=10, sticky=tk.W + tk.E)

        ttk.Label(self.root, text="Zodiac:").grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        self.zodiac_entry = ttk.Combobox(self.root, values=list(zodiac_data.keys()))
        self.zodiac_entry.grid(row=1, column=1, pady=5, padx=10, sticky=tk.W + tk.E)

        tk.Label(self.root, text="Horoscope: ").grid(row=2, column=0)
        tk.Label(self.root, text="Lucky Number: ").grid(row=3, column=0)
        tk.Label(self.root, text="Lucky Color: ").grid(row=4, column=0)
        tk.Label(self.root, text="Compatibility: ").grid(row=5, column=0)

        self.horoscope_var = tk.StringVar()
        self.lucky_number_var = tk.StringVar()
        self.lucky_color_var = tk.StringVar()
        self.compatibility_var = tk.StringVar()
 
        ttk.Label(self.root, textvariable=self.horoscope_var, wraplength=300, justify=tk.LEFT).grid(row=2, column=1,
                                                                                                 pady=5, padx=10,
                                                                                                 sticky=tk.W)
        ttk.Label(self.root, textvariable=self.lucky_number_var).grid(row=3, column=1, pady=5, padx=10, sticky=tk.W)
        ttk.Label(self.root, textvariable=self.lucky_color_var).grid(row=4, column=1, pady=5, padx=10, sticky=tk.W)
        ttk.Label(self.root, textvariable=self.compatibility_var, wraplength=300, justify=tk.LEFT).grid(row=5, column=1,
                                                                                                       pady=5, padx=10,
                                                                                                       sticky=tk.W)

        ttk.Button(self.root, text="Submit", command=self.get_zodiac_data).grid(row=6, column=0, columnspan=2, pady=10,
                                                                               padx=10)


        ttk.Button(self.root, text="Login as Admin", command=self.login_as_admin).grid(row=7, column=0, columnspan=2,
                                                                                     pady=10, padx=10)

    def get_zodiac_data(self):
        user_name = self.name_entry.get()
        user_sign = self.zodiac_entry.get().lower()

        if user_sign in zodiac_data:
            data = zodiac_data[user_sign]

            self.horoscope_var.set(f"Your horoscope for {user_sign}: {data['horoscope']}")
            self.lucky_number_var.set(f"Your lucky number is: {data['lucky_number']}")
            self.lucky_color_var.set(f"Your lucky color is: {data['lucky_color']}")
            self.compatibility_var.set(f"Compatibility with: {', '.join(data['compatibility'])}")

            self.database.insert_data(
                user_name,
                user_sign,
                data['horoscope'],
                data['lucky_number'],
                data['lucky_color'],
                ', '.join(data['compatibility'])
            )
        else:
            self.horoscope_var.set("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.")
            self.lucky_number_var.set("-")
            self.lucky_color_var.set("-")
            self.compatibility_var.set("-")

    def login_as_admin(self):
        admin_password = "valt"
        password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")

        if password == admin_password:
            self.is_admin = True
            self.create_admin_widgets()
        else:
            messagebox.showerror("Admin Login", "Invalid password. Try again.")


    def create_admin_widgets(self):
        ttk.Label(self.root, text="Admin Section", font=("Helvetica", 16, "bold")).grid(row=8, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Delete Latest Entries", command=self.delete_latest_entries).grid(row=9, column=0, columnspan=2,pady=10, padx=10)      
        ttk.Button(self.root, text="View Entries", command=self.view_entries).grid(row=11, column=0, columnspan=2, pady=10, padx=10)

    def view_entries(self):
        entries = self.database.get_all_entries()
        if entries:
            self.show_entries(entries)
        else:
            messagebox.showinfo("View Entries", "No entries found.")

    def delete_latest_entries(self):
        num_entries = 1
        self.database.delete_latest_entries(num_entries)

    def show_entries(self, entries):
        # Display entries in a new window
        window = tk.Toplevel(self.root)
        window.title("All Entries")

        ttk.Label(window, text="All Entries", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        for i, entry in enumerate(entries, start=1):
            ttk.Label(window, text=f"Entry {i}").grid(row=i, column=0, pady=5, padx=10, sticky=tk.W)
            ttk.Label(window, text=f"ID: {entry[0]} | Name: {entry[1]} | Zodiac: {entry[2]}").grid(row=i, column=1, pady=5, padx=10, sticky=tk.W)
            ttk.Button(window, text="Update", command=lambda entry_id=entry[0]: self.update_entry_dialog(entry_id)).grid(row=i, column=2, pady=5, padx=10)
            ttk.Button(window, text="Delete", command=lambda id=entry[0]: self.delete_entry(id)).grid(row=i, column=3, pady=5, padx=10)

    def delete_entry(self, entry_id):
        result = messagebox.askokcancel("Delete Entry", f"Do you want to delete entry with ID {entry_id}?")
        if result:
            self.database.delete_entry(entry_id)
            messagebox.showinfo("Delete Entry", f"Entry with ID {entry_id} deleted successfully.")

    def update_entry_dialog(self, entry_id):
        updated_name = simpledialog.askstring("Update Entry", "Enter updated name:")
        updated_zodiac_sign = simpledialog.askstring("Update Entry", "Enter updated zodiac sign:")
        updated_horoscope = simpledialog.askstring("Update Entry", "Enter updated horoscope:")
        updated_lucky_number = simpledialog.askstring("Update Entry", "Enter updated lucky number:")
        updated_lucky_color = simpledialog.askstring("Update Entry", "Enter updated lucky color:")
        updated_compatibility = simpledialog.askstring("Update Entry", "Enter updated compatibility:")

        if updated_name is not None:
            self.database.update_entry(entry_id, updated_name, updated_zodiac_sign, updated_horoscope, updated_lucky_number, updated_lucky_color, updated_compatibility)



    def get_entry_data(self, entry_id):
        try:
            with self.database.mydb.cursor() as cursor:
                cursor.execute("SELECT * FROM horoscope WHERE id=%s", (entry_id,))
                entry_data = cursor.fetchone()
                return entry_data
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def show_entry_data(self, entry_data):
        # Display entry data in the GUI
        if entry_data:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, entry_data[1])
            self.zodiac_entry.set(entry_data[2])
            self.horoscope_var.set(f"Your horoscope for {entry_data[2]}: {entry_data[3]}")
            self.lucky_number_var.set(f"Your lucky number is: {entry_data[4]}")
            self.lucky_color_var.set(f"Your lucky color is: {entry_data[5]}")
            self.compatibility_var.set(f"Compatibility with: {entry_data[6]}")
        else:
            messagebox.showerror("Show Entry Data", "Entry data not found.")

def update_entry(self, entry_id, user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility):
    try:
        with self.mydb.cursor() as cursor:
            sql = "UPDATE horoscope SET user_name=%s, zodiac_sign=%s, horoscope=%s, lucky_number=%s, lucky_color=%s, compatibility=%s WHERE id=%s"
            val = (user_name, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility, entry_id)
            cursor.execute(sql, val)
        self.mydb.commit()
        print(f"Entry {entry_id} updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print(f"Failed to update entry {entry_id}.")



if __name__ == "__main__":
    zodiac_data = {
        "aries": {
            "horoscope":
            "You are energetic and confident today. Take the lead in your activities and make the most of your day.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Red",
            "compatibility": ["Leo", "Sagittarius", "Gemini"],
        },
        "taurus": {
            "horoscope": "Your determination and practicality will help you achieve your goals. Stick to your plans and stay grounded.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Green",
            "compatibility": ["Virgo", "Capricorn", "Pisces"],
        },
        "gemini": {
            "horoscope":
            "You're in a social mood today. Communicate and express yourself clearly to connect with others.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Yellow",
            "compatibility": ["Libra", "Aquarius", "Aries"],
        },
        "cancer": {
            "horoscope":
            "Emotions may run high today. Take some time for self-care and reflect on your feelings.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Blue",
            "compatibility": ["Scorpio", "Pisces", "Taurus"],
        },
        "leo": {
            "horoscope":
            "You're in the spotlight today. Use your charisma and creativity to shine in your endeavors.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Orange",
            "compatibility": ["Aries", "Sagittarius", "Libra"],
        },
        "virgo": {
            "horoscope":
            "Pay attention to details and stay organized. Your practical approach will lead to success.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Brown",
            "compatibility": ["Taurus", "Capricorn", "Cancer"],
        },
        "libra": {
            "horoscope":
            "Balance is essential for you today. Strive for harmony in your relationships and decisions.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Pink",
            "compatibility": ["Sagittarius", "Aquarius", "Leo"],
        },
        "scorpio": {
            "horoscope":
            "Your intuition is strong today. Trust your instincts and pursue your passions with intensity.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Purple",
            "compatibility": ["Cancer", "Pisces", "Virgo"],
        },
        "sagittarius": {
            "horoscope":
            "Adventure and exploration are favored today. Seek new experiences and broaden your horizons.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Turquoise",
            "compatibility": ["Capricorn", "Libra", "Aquarius"],
        },
        "capricorn": {
            "horoscope":
            "Focus on your responsibilities and goals. Hard work will lead to long-term success.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Black",
            "compatibility": ["Sagittarius", "Virgo", "Pisces"],
        },
        "aquarius": {
            "horoscope":
            "You may feel a sense of rebellion today. Embrace your uniqueness and think outside the box.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Silver",
            "compatibility": ["Gemini", "Libra", "Sagittarius"],
        },
        "pisces": {
            "horoscope":
            "Your creativity and empathy shine today. Connect with others on a deep emotional level.",
            "lucky_number": random.randint(1, 100),
            "lucky_color": "Sea Green",
            "compatibility": ["Taurus", "Cancer", "Scorpio"],
        },
    }

    database = ZodiacDatabase(host="localhost", user="root", password="valt", database="user_zodiac")

    root = tk.Tk()
    app = ZodiacApp(root, database)

    root.mainloop()

