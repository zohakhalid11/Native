def main():
    # Ask for the user's name
    name = input("What is your name? ")

    # Create a personalized message
    message = f"Hello {name}, welcome to the program"

    # Print the personalized message
    print(message)

# This checks if the script is being run directly
if __name__ == "__main__":
    main()
# This script asks the user for their name and prints a personalized greeting.
# 
# Code Breakdown:
# 1. The `main()` function contains the core logic of the program.
# 2. It uses `input()` to prompt the user for their name.
# 3. It stores the user's input in the variable `name`.
# 4. It then builds a message using an f-string to include the name.
# 5. The message is printed using `print()`.
# 6. The `if __name__ == "__main__":` line ensures that `main()` only runs 
#    when the script is executed directly (not when imported as a module).
