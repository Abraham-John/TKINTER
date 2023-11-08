import random
import tkinter as tk

# Define a dictionary of horoscopes, lucky numbers, lucky colors, and compatibility for each zodiac sign
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
    # Add other zodiac signs with horoscopes, lucky numbers, lucky colors, and compatibility
}

# Function to get and display horoscope, lucky number, lucky color, and compatibility
def get_horoscope():
    user_sign = entry.get()
    if user_sign in zodiac_data:
        data = zodiac_data[user_sign]
        horoscope_text.set(f"Your horoscope for {user_sign}: {data['horoscope']}")
        lucky_number_text.set(f"Your lucky number is: {data['lucky_number']}")
        lucky_color_text.set(f"Your lucky color is: {data['lucky_color']}")
        compatibility_text.set(f"Compatibility with: {', '.join(data['compatibility'])}")
    else:
        horoscope_text.set("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.")

# Create the tkinter window
root = tk.Tk()
root.title("Zodiac Horoscope")

# Entry field for user to enter their zodiac sign
entry = tk.Entry(root)
entry.pack()

# Button to get horoscope
get_button = tk.Button(root, text="Get Horoscope", command=get_horoscope)
get_button.pack()

# Text variables to display the horoscope, lucky number, lucky color, and compatibility
horoscope_text = tk.StringVar()
lucky_number_text = tk.StringVar()
lucky_color_text = tk.StringVar()
compatibility_text = tk.StringVar()

# Labels to display the horoscope, lucky number, lucky color, and compatibility
horoscope_label = tk.Label(root, textvariable=horoscope_text)
horoscope_label.pack()
lucky_number_label = tk.Label(root, textvariable=lucky_number_text)
lucky_number_label.pack()
lucky_color_label = tk.Label(root, textvariable=lucky_color_text)
lucky_color_label.pack()
compatibility_label = tk.Label(root, textvariable=compatibility_text)
compatibility_label.pack()

root.mainloop()
