import random

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

user_sign = input("Enter your zodiac sign: ")

if user_sign in zodiac_data:
    data = zodiac_data[user_sign]
    horoscope = data["horoscope"]
    lucky_number = data["lucky_number"]
    lucky_color = data["lucky_color"]
    compatibility = data["compatibility"]
    print(f"Your horoscope for {user_sign}: {horoscope}")
    print(f"Your lucky number is: {lucky_number}")
    print(f"Your lucky color is: {lucky_color}")
    print(f"Compatibility with: {', '.join(compatibility)}")
else:
    print("Sorry, I don't have information for that zodiac sign. Please enter a valid sign.")
