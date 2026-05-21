import re, random

from colorama import Fore, init
from matplotlib import text

destinations = {

    "beaches": ["Bali", "Maldives", "Phuket"],

    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

    "cities": ["Tokyo", "Paris", "New York"]

}

jokes=[
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

def normalize_input(user_input):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.Cyan + "TravelBot: Beaches, mountains, or cities?")
    preference=input(Fore.YELLOW + "You:")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestions=random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestions}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer=input(Fore.YELLOW + "You:").lower()

        if answer=="yes":
            print(Fore.GREEN + "TravelBot: Great! Enjoy your trip!")
        elif answer=="no":
            print(Fore.RED + "TravelBot: No worries! Let's try again.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Let's try again.")
            recommend()

    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that. Please choose from beaches, mountains, or cities.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location=normalize_input(input(Fore.YELLOW + "You:"))
    print(Fore.CYAN + "TravelBot: How long?")
    days=input(Fore.YELLOW + "You:")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} in {location}:")
    print(Fore.GREEN + "- Pack light and versatile clothing.")
    print(Fore.GREEN + "- Don't forget your chargers and adapters.")
    print(Fore.GREEN + "- Bring a reusable water bottle.")
    print(Fore.GREEN + "- Check the weather forecast before you go.")

def tell_joke():
    print(Fore.CYAN + "TravelBot: Here's a travel joke for you: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "TravelBot: I can help you with the following commands:")
    print(Fore.MAGENTA + "- recommend: Get travel recommendations based on your preferences.")
    print(Fore.MAGENTA + "- packing: Get packing tips for your trip.")
    print(Fore.MAGENTA + "- joke: Hear a travel joke.")
    print(Fore.MAGENTA + "- help: Display this help message.")

def chat():
    print(Fore.CYAN + "TravelBot: Hi! I'm TravelBot.")
    name=input(Fore.YELLOW + "TravelBot: What's your name?")
    print(Fore.CYAN + f"TravelBot: Nice to meet you, {name}!")

    show_help()

    while True:
        user_input=input(Fore.YELLOW + f"{name}: ")
        user_input=normalize_input(user_input)

        if "reccomend" in user_input or "suggest" in user_input:
            recommend()
        elif "packing" in user_input or "pack" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "quit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chat()