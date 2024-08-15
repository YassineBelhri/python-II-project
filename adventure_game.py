
import random
import time

# Lists of potential foes, weapons, and gadgets
villains = ["Ruler A", "Ruler B", "Ruler C"]
gear_options = ["Machine Gun", "Rocket Launcher", "Precision Rifle"]
tools = ["Camouflage Cloak", "Power Elixir", "Defense Shield"]


def display_message_with_delay(message):
    """
    Print a message with a slight pause for dramatic effect.

    Args:
        message (str): The message to be printed.
    """
    print(message)
    time.sleep(1)


def game_intro(villain):
    """
    Introduce the game scenario to the player.

    Args:
        villain (str): The antagonist to be confronted.
    """
    display_message_with_delay("You have been thrust into a risky scenario.")
    display_message_with_delay(f"A tyrant known as {villain} stands in your way.")
    display_message_with_delay("Prepare yourself for imminent confrontation.")


def engage_battle(villain, weapon):
    """
    Simulate the battle against the selected villain.

    Args:
        villain (str): The foe you are confronting.
        weapon (str): The weapon you have selected.
    """
    display_message_with_delay(f"{villain} charges at you with relentless force.")
    if weapon == "Machine Gun":
        display_message_with_delay(
            f"Sadly, your {weapon} isn't enough to defeat {villain}."
        )
        return 'defeated'
    else:
        display_message_with_delay(
            f"Using your {weapon}, you overpower {villain}."
        )
        return 'victorious'


def replay_decision():
    """
    Ask the player if they wish to replay the game.

    Returns:
        bool: True if the player wants another round, False otherwise.
    """
    response = ''
    while response not in ['y', 'n']:
        response = input("Do you want to try again? (y/n) ").lower()
    if response == 'n':
        display_message_with_delay("Thank you for playing! Farewell.")
        return False
    elif response == 'y':
        display_message_with_delay(
            "Awesome! Let's dive into a new adventure..."
        )
        return True


def weapon_selection():
    """
    Allow the player to choose a weapon for the upcoming battle.

    Returns:
        str: The chosen weapon.
    """
    display_message_with_delay("You scour the area for a weapon:")
    for idx, weapon in enumerate(gear_options, start=1):
        display_message_with_delay(f"{idx}. {weapon}")
    while True:
        choice = input(
            "Choose your weapon by entering the corresponding number: "
        )
        if choice.isdigit() and 1 <= int(choice) <= len(gear_options):
            return gear_options[int(choice) - 1]
        else:
            display_message_with_delay(
                "Invalid input. Please select a valid option."
            )


def start_adventure():
    """Launch the game and control the gameplay loop."""
    while True:
        villain = random.choice(villains)
        weapon = weapon_selection()

        game_intro(villain)

        result = engage_battle(villain, weapon)

        if result == 'victorious' or result == 'defeated':
            if result == 'victorious':
                display_message_with_delay(
                    "You've triumphed over the tyrant! Well done!"
                )
            else:
                display_message_with_delay(
                    "Unfortunately, you've been defeated."
                )

        if not replay_decision():
            break


# Begin the game
start_adventure()
