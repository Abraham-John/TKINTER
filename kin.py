import random
import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

zodiac_data = {
    "Aries": {
        "horoscope": "You are energetic and confident today. Take the lead in your activities and make the most of your day.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Red",
        "compatibility": ["Leo", "Sagittarius", "Gemini"],
    },
    "Taurus": {
        "horoscope": "Your determination and practicality will help you achieve your goals. Stick to your plans and stay grounded.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Green",
        "compatibility": ["Virgo", "Capricorn", "Pisces"],
    },
    "Gemini": {
        "horoscope": "You're in a social mood today. Communicate and express yourself clearly to connect with others.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Yellow",
        "compatibility": ["Libra", "Aquarius", "Aries"],
    },
    "Cancer": {
        "horoscope": "Emotions may run high today. Take some time for self-care and reflect on your feelings.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Blue",
        "compatibility": ["Scorpio", "Pisces", "Taurus"],
    },
    "Leo": {
        "horoscope": "You're in the spotlight today. Use your charisma and creativity to shine in your endeavors.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Orange",
        "compatibility": ["Aries", "Sagittarius", "Libra"],
    },
    "Virgo": {
        "horoscope": "Pay attention to details and stay organized. Your practical approach will lead to success.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Brown",
        "compatibility": ["Taurus", "Capricorn", "Cancer"],
    },
    "Libra": {
        "horoscope": "Balance is essential for you today. Strive for harmony in your relationships and decisions.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Pink",
        "compatibility": ["Gemini", "Aquarius", "Leo"],
    },
    "Scorpio": {
        "horoscope": "Your intuition is strong today. Trust your instincts and pursue your passions with intensity.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Purple",
        "compatibility": ["Cancer", "Pisces", "Virgo"],
    },
    "Sagittarius": {
        "horoscope": "Adventure and exploration are favored today. Seek new experiences and broaden your horizons.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Turquoise",
        "compatibility": ["Aries", "Leo", "Aquarius"],
    },
    "Capricorn": {
        "horoscope": "Focus on your responsibilities and goals. Hard work will lead to long-term success.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Black",
        "compatibility": ["Taurus", "Virgo", "Pisces"],
    },
    "Aquarius": {
        "horoscope": "You may feel a sense of rebellion today. Embrace your uniqueness and think outside the box.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Silver",
        "compatibility": ["Gemini", "Libra", "Sagittarius"],
    },
    "Pisces": {
        "horoscope": "Your creativity and empathy shine today. Connect with others on a deep emotional level.",
        "lucky_number": random.randint(1, 10),
        "lucky_color": "Sea Green",
        "compatibility": ["Taurus", "Cancer", "Scorpio"],
    },
}


def get_lolu():
    user_sign = entry.get()
    if user_sign in zodiac_data:
        data = zodiac_data[user_sign]

        Horoscope.set(f"Your horoscope for {user_sign}: {data['horoscope']}") 
        lucky_number.set(f"Your lucky number is: {data['lucky_number']}") 
        lucky_color.set(f"Your lucky color is: {data['lucky_color']}") 
        compatibility.set(f"Compatibility with: {', '.join(data['compatibility'])}")
    else:
        Horoscope.set("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.")
        lucky_number.set("")  
        lucky_color.set("")   
        compatibility.set("") 

root = tk.Tk()
root.title("Horoscope")
root.geometry("750x750")

cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_zodiac (zodiac_sign VARCHAR(255), horoscope TEXT, lucky_number INT, lucky_color VARCHAR(255), compatibility TEXT)")
mydb.commit()

entry = tk.Entry(root)
entry.pack()


tk.Label(root, text="zodiac ").pack()

tk.Label(root, text="Horoscope: ").pack() 
tk.Label(root, text="lucky_number: ").pack() 
tk.Label(root, text="lucky_color: ").pack() 
tk.Label(root, text="compatibility: ").pack()

Horoscope = tk.StringVar()
lucky_number = tk.StringVar()
lucky_color= tk.StringVar()
compatibility= tk.StringVar()

Horoscope_label = tk.Label(root , textvariable=Horoscope)
lucky_number_label = tk.Label(root , textvariable=lucky_number)
lucky_color_label = tk.Label(root , textvariable=lucky_color)
compatibility_label = tk.Label(root , textvariable=compatibility)


Horoscope_label.pack()
lucky_number_label.pack()
lucky_color_label.pack()
compatibility_label.pack()

tk.Button(text="submit", command=get_lolu).pack()
root.mainloop()
