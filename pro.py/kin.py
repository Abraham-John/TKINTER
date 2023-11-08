import random
import tkinter as tk


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
        Horoscope.set("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.") # type: ignore

root = tk.Tk()
root.title("Horoscope")
root.geometry("750x750")


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
