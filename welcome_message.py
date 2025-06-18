def main():
    # Ask for the user's name
    name = input("What is your name? ")

    # Check if the name is Sasha
    if name.lower() == "sasha":

        print("Hey it's my awesome boss Sasha")
    else:
        # Create a personalized message
        message = f"Hello {name}, welcome to the program"
        print(message)

# This checks if the script is being run directly
if __name__ == "__main__":
    main()

