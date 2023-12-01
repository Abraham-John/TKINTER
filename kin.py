import random
import tkinter as tk
import mysql.connector

class ZodiacDatabase:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )


    def insert_data(self, zodiac_sign, horoscope, lucky_number, lucky_color, compatibility):
        try:
            with self.mydb.cursor() as cursor:
                sql = "INSERT INTO horoscope (zodiac_sign, horoscope, lucky_number, lucky_color, compatibility) VALUES (%s, %s, %s, %s, %s)"
                val = (zodiac_sign, horoscope, lucky_number, lucky_color, compatibility)
                cursor.execute(sql, val)
            self.mydb.commit()
            print("Data successfully saved to the database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Failed to save data to the database.")


class ZodiacApp:
    def __init__(self, root, database):
        self.root = root
        self.database = database
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0, column=1)

        tk.Label(self.root, text="ZODIAC").grid(row=0, column=0)

        tk.Label(self.root, text="Horoscope: ").grid(row=1, column=0)
        tk.Label(self.root, text="Lucky Number: ").grid(row=2, column=0)
        tk.Label(self.root, text="Lucky Color: ").grid(row=3, column=0)
        tk.Label(self.root, text="Compatibility: ").grid(row=4, column=0)

        self.horoscope_var = tk.StringVar()
        self.lucky_number_var = tk.StringVar()
        self.lucky_color_var = tk.StringVar()
        self.compatibility_var = tk.StringVar()

        tk.Label(self.root, textvariable=self.horoscope_var).grid(row=1, column=1)
        tk.Label(self.root, textvariable=self.lucky_number_var).grid(row=2, column=1)
        tk.Label(self.root, textvariable=self.lucky_color_var).grid(row=3, column=1)
        tk.Label(self.root, textvariable=self.compatibility_var).grid(row=4, column=1)

        tk.Button(self.root, text="Submit", command=self.get_zodiac_data).grid(row=5, column=0, columnspan=2)

    def get_zodiac_data(self):
        user_sign = self.entry.get().lower()
        if user_sign in zodiac_data:
            data = zodiac_data[user_sign]

            self.horoscope_var.set(f"Your horoscope for {user_sign}: {data['horoscope']}")
            self.lucky_number_var.set(f"Your lucky number is: {data['lucky_number']}")
            self.lucky_color_var.set(f"Your lucky color is: {data['lucky_color']}")
            self.compatibility_var.set(f"Compatibility with: {', '.join(data['compatibility'])}")

            # Save the values to the MySQL database
            self.database.insert_data(user_sign, data['horoscope'], data['lucky_number'], data['lucky_color'],
                                      ', '.join(data['compatibility']))
        else:
            self.horoscope_var.set("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.")
            self.lucky_number_var.set("-")
            self.lucky_color_var.set("-")
            self.compatibility_var.set("-")

if __name__ == "__main__":
    zodiac_data = {
    "aries": {
        "horoscope": "You are energetic and confident today. Take the lead in your activities and make the most of your day.",
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
        "horoscope": "You're in a social mood today. Communicate and express yourself clearly to connect with others.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Yellow",
        "compatibility": ["Libra", "Aquarius", "Aries"],
    },
    "cancer": {
        "horoscope": "Emotions may run high today. Take some time for self-care and reflect on your feelings.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Blue",
        "compatibility": ["Scorpio", "Pisces", "Taurus"],
    },
    "leo": {
        "horoscope": "You're in the spotlight today. Use your charisma and creativity to shine in your endeavors.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Orange",
        "compatibility": ["Aries", "Sagittarius", "Libra"],
    },
    "virgo": {
        "horoscope": "Pay attention to details and stay organized. Your practical approach will lead to success.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Brown",
        "compatibility": ["Taurus", "Capricorn", "Cancer"],
    },
    "libra": {
        "horoscope": "Balance is essential for you today. Strive for harmony in your relationships and decisions.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Pink",
        "compatibility": ["Sagittarius", "Aquarius", "Leo"],
    },
    "scorpio": {
        "horoscope": "Your intuition is strong today. Trust your instincts and pursue your passions with intensity.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Purple",
        "compatibility": ["Cancer", "Pisces", "Virgo"],
    },
    "sagittarius": {
        "horoscope": "Adventure and exploration are favored today. Seek new experiences and broaden your horizons.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Turquoise",
        "compatibility": ["Capricorn", "Libra", "Aquarius"],
    },
    "capricorn": {
        "horoscope": "Focus on your responsibilities and goals. Hard work will lead to long-term success.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Black",
        "compatibility": ["Sagittarius", "Virgo", "Pisces"],
    },
    "aquarius": {
        "horoscope": "You may feel a sense of rebellion today. Embrace your uniqueness and think outside the box.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Silver",
        "compatibility": ["Gemini", "Libra", "Sagittarius"],
    },
    "pisces": {
        "horoscope": "Your creativity and empathy shine today. Connect with others on a deep emotional level.",
        "lucky_number": random.randint(1, 100),
        "lucky_color": "Sea Green",
        "compatibility": ["Taurus", "Cancer", "Scorpio"],
    },}

    database = ZodiacDatabase(host="localhost", user="root", password="valt", database="user_zodiac")

    root = tk.Tk()
    root.title("Horoscope")
    root.geometry("400x200")

    app = ZodiacApp(root, database)

    root.mainloop()