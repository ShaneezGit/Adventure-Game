import time

# Function to prompt the user with a given prompt and list of options
    # Display prompt to the user and get user input
    # Check if user input is in options
    # Display error message for invalid input
def prompt_user(prompt, options):
    """
    Prompt the user with a given prompt and list of options.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "":
            print("Please pprovide an input.")
        elif user_input.lower() in options:
            return user_input.lower()
        else:
            print("Invalid input. Please try again.")

# Main function to run the adventure game
    # Get user's name
    # Display welcome message with user's name
    # Get user's chosen direction (left or right)
    # Check user's chosen direction
        # Get user's action at the river (walk or swim)
        # Check user's action at the river
            # Display message if user swims across the river
            # Display message if user walks around the river
        # Get user's action at the bridge (cross or back)
        # Check user's action at the bridge 
            # Display message if user heads back from the bridge
            # Get user's decision to talk to the stranger (yes or no)
            # Check user's decision to talk to the stranger
                # Display message if user talks to the stranger
                # Display message if user ignores the stranger
    # Display message for invalid direction
    # Display thank you message with the user's name
def main():
    name = input("Type your name: ")
    time.sleep(0.5)
    print("\n** Welcome", name, "to this adventure! **")

    time.sleep(1)

    direction = prompt_user(
        "\nYou are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ",
        ["left", "right"]
    )

    if direction == "left":
        action = prompt_user(
            "\nYou come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim accross: ",
            ["walk", "swim"]
        )
        if action == "swim":
            print("\nYou swam across and were eaten by an alligator!")
        elif action == "walk":
            print("\nYou walked for many miles, ran out of water and you lost the game.")
    elif direction == "right":
        action = prompt_user(
            "\nYou come to a bridge, it looks wobbly, do you want to cross it or head back? Type 'cross' to cross it or 'back' to head back: ",
            ["cross", "back"]
        )
        if action == "back":
            print("\nYou go back and lose. ")
        elif action == "cross":
            talk_stranger = prompt_user(
                "\nYou cross a bridge and meet a stranger. Do you talk to them? Type 'yes' or 'no': ",
                ["yes", "no"]
            )
            if talk_stranger == "yes":
                print("\nYou talk to the stranger and they give gold. You WIN!!")
            elif talk_stranger == "no":
                print("\nYou ignore the stranger and they are offended and you lose.")

    else:
        print('\nNot a valid option. You lose.')

    print("\nThank you for trying", name, "!")
    time.sleep(1)
    print("Goodbye!")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()