# Prince Djine
# 12-6-8-2025
# Final Projectttttttt amazing course coming to an end sadly - Treasure Cave Adventure Game
# This program is a simple text adventure where the player explores a cave,
# collects treasure, avoids hazards, and tries to escape with enough gold.


import random
import time

# ---------------------------
# FUNCTIONS
# ---------------------------

def intro():
    print("Welcome to the Treasure Cave Adventure!")
    time.sleep(1)
    print("You enter a dark cave with only a torch...")
    time.sleep(1)
    print("Your goal is to escape with at least 50 gold.\n")
    time.sleep(1)

def explore(inventory, gold):
    """Handles a random cave event."""
    print("\nYou move deeper into the cave...")
    time.sleep(1)

    event = random.randint(1, 4)

    if event == 1:
        print("You found a small treasure chest! +15 gold")
        gold += 15

    elif event == 2:
        print("A slime monster attacks!")
        time.sleep(1)
        print("You fight it off but drop 10 gold...")
        gold -= 10
        if gold < 0:
            gold = 0

    elif event == 3:
        print("You find a healing herb and place it in your inventory.")
        inventory.append("herb")

    elif event == 4:
        print("You set off a trap! You lose some time but escape safely.")

    return inventory, gold

def use_item(inventory, gold):
    """Let the player use an item from inventory (if any)."""
    if len(inventory) == 0:
        print("You have no items to use.")
        return inventory, gold

    print("\nInventory:", inventory)
    choice = input("Type 'herb' to use it or 'back' to cancel: ")

    if choice == "herb":
        if "herb" in inventory:
            print("You use the herb and gain +10 gold!")
            gold += 10
            inventory.remove("herb")
        else:
            print("You don't have that item.")
    else:
        print("Going back...")

    return inventory, gold

def main():
    inventory = []
    gold = 0
    intro()

    exploring = True

    while exploring:
        print("\nGold:", gold)
        print("Inventory:", inventory)
        print("\nChoose an action:")
        print("1. Explore deeper")
        print("2. Use an item")
        print("3. Try to escape the cave")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory, gold = explore(inventory, gold)

        elif choice == "2":
            inventory, gold = use_item(inventory, gold)

        elif choice == "3":
            print("\nYou attempt to escape...")
            time.sleep(1)
            if gold >= 50:
                print("You escaped with enough treasure! You win!")
            else:
                print("You don't have enough gold. You fail to escape and die from being broke.")
            exploring = False

        else:
            print("Invalid choice. Try again.")

    print("\nThanks for playing Treasure Cave Adventure!")


# Call main()
main()
