import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# List of fun facts or quotes
fun_facts = [
    "Did you know? Python was named after Monty Python.",
    "AI is changing the world — and you’re learning it!",
    "Fun fact: The first computer bug was an actual moth.",
    "Your name has now been logged by the Matrix... just kidding!",
    "Keep learning — future you will thank you!"
]

# Typing effect function
def type_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # Animated greeting
    type_print(Fore.CYAN + "\n👋 Hello! Welcome to the Interactive Greeting Program!", 0.04)
    type_print(Fore.CYAN + "Let's get to know each other. 😄", 0.04)

    while True:
        name = input(Fore.YELLOW + "\nWhat’s your name? ").strip()

        # Validate input
        while not name:
            name = input(Fore.RED + "Oops! Please enter a valid name: ").strip()

        # Personalized greeting
        print(Fore.GREEN + f"\nHi {name}, great to meet you! 🚀")
        
        # Print a random fun fact
        print(Fore.MAGENTA + random.choice(fun_facts))

        # Ask if they want to do it again
        again = input(Fore.BLUE + "\nWould you like to greet someone else? (y/n): ").lower()
        if again != 'y':
            type_print(Fore.CYAN + "\nThanks for using the program. See you next time!", 0.04)
            break

if __name__ == "__main__":
    main()












