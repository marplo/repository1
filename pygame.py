inventory = []
# This is the list of items we have in our inventory.
# To add to it:
# inventory.append("Some pocket lint")
# To remove from it:
# inventory.remove("Some pocket lint")
# To determine if a player has an item: (This is a bit tricky)
# try:
# inventory.index("Some pocket lint") # Creates an error if it doesn't exist.
# print("The player has the item!")
# except:
# print("The player doesn't have the item")

def main_room():
    print("you are in a cold damp room. there are 2 doors and 1 chest what will you do?")
print(
" You can do the following things:\n"
" * 'l' - Explore the door to your left.\n"
" * 'r' - Explore the door to your right.\n"
" * 'o' - Open the chest in front of you.\n"
" * 'i' - Examine your inventory.\n"
" * 'a' - Look around.\n")
# Take the player's choice.
choice = input("What do you do?: ")
# Determine what they picked an act on it.
if choice == 'l':
print("You chose to enter the door to the left!\n")
left_room()
elif choice == 'r':
print("You chose to enter the door to your right!\n")
right_room()
elif choice == 'o':
print("You chose to open the chest in front of you! You discover it contains a red LED flashlight, including batteries.\n")
# Add a flashlight to the player's inventory.
inventory.append("Red LED Flashlight")
# Start over again.
main_room()

elif choice == 'a':
print("You chose to look around! You see a desk.On the desk you notice a camera\n")
# Add a flashlight to the player's inventory.
inventory.append("Camera")
# Start over again.
main_room()
elif choice == 'i':
if len(inventory) != 0:
print("You have the following items in your inventory:")
for item in inventory:
print(" " + item)
else:
print("You don't have anything in your inventory")
print("\n")
main_room();

def left_room():
# If the player doesn't have the flashlight already, they only see darkness.
try:
inventory.index("Red LED Flashlight")
# The code from here until "except" only runs if they have the flashlight.
print("The room is totally empty except for a lone flask marked \"SHRINKING POTION, DO NOT DRINK\"")
# Display their options.
print(
" You can do the following things:\n"
" * 'd' - Drink the potion.\n"
" * 't' - Take the potion and put it in your inventory.\n"
" * 'r' - Return to the main room.")
choice = input("What do you do, explorer?: ")
if choice == 'd':
print("You drink the potion and become several millimeters smaller, at least you think. You turn around and go back.\n")
main_room()
elif choice == 't':
inventory.append("Shrinking Potion")
print("You take the potion, and stuff it into your pocket, then turn around and go back.\n")
main_room()
elif choice == 'r':
print("You return to the main room.\n")
main_room()
except:
print("You don't see anything in the room, it's way to dark. You carefully close it and turn back around.\n")
# Send them back to the main room.
main_room()

def right_room():
inventory.index("Red LED Flashlight")
print("You see a sign on the door that says that the room is \"Under Construction\" but decide to look anyways...\n"
"Inside, you find a bare room with weird code flowing around the walls and changing every second. This is probably not a safe place to be.\n"
"You turn back, and go to the main room.\n")
if inventory.index("Camera"):
print("you quickly take a picture of the code on the walls")
inventory.append("Picture of coding on the walls")
main_room()

# Since we're defining the main_room as a function, we need to call it, otherwise it won't get called!
main_room()