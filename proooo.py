import random
import tkinter as tk
from tkinter import ttk, W, E  ,simpledialog, messagebox
import mysql.connector

class ZodiacDatabase:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.create_table()

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
            print("Table created or already exists.")
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

class ZodiacApp:
    def __init__(self, root, database):
        self.root = root
        self.database = database
        self.is_admin = False  
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Your Name:").grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, pady=5, padx=10, sticky=tk.W + E)

        ttk.Label(self.root, text="Zodiac:").grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        self.zodiac_entry = ttk.Combobox(self.root, values=list(zodiac_data.keys()))
        self.zodiac_entry.grid(row=1, column=1, pady=5, padx=10, sticky=tk.W + E)

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
        ttk.Button(self.root, text="Delete Latest Entries", command=self.delete_latest_entries).grid(row=8, column=0,
                                                                                                      columnspan=2,
                                                                                                      pady=10, padx=10)

    def delete_latest_entries(self):
        num_entries = 1  
        self.database.delete_latest_entries(num_entries)


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
