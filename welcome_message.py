from colorama import Fore, Style, init
import random

init(autoreset=True)  # Initialize colorama

special_names = {
    "sasha": "Hey, it’s my awesome boss Sasha!",
    "alex": "Hello Alex, the coding wizard!",
    "jordan": "Yo Jordan! Ready to crush it today?"
}

quotes = [
    "Keep pushing your limits!",
    "Every bug is a step closer to mastery.",
    "Code, test, repeat — success is near!",
    "Your AI journey is just beginning, stay curious!",
    "Mistakes are proof you're trying."
]

def get_special_greeting(name):
    name_lower = name.lower()
    for special in special_names:
        if special in name_lower:
            return special_names[special]
    return None

def main():
    print(Fore.CYAN + "Welcome to the Interactive Greeting Program! Type 'exit' to quit.\n")

    while True:
        name = input(Fore.YELLOW + "What is your name? ").strip()
        if name.lower() == "exit":
            print(Fore.GREEN + "Goodbye! Keep coding strong!")
            break

        if not name:
            print(Fore.RED + "Oops! You didn't enter a name. Try again.")
            continue

        special_msg = get_special_greeting(name)
        if special_msg:
            print(Fore.MAGENTA + special_msg)
        else:
            print(Fore.BLUE + f"Hello {name}, welcome to the program!")

        print(Fore.GREEN + random.choice(quotes) + "\n")


if __name__ == "__main__":
    main()


