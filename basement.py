#
# Gavin McKenzie
# 3/7/24
# Code for the Basement floor of the game
# import MainFloor
from time import sleep
from os import system
import Ascii_artr

INVENTORY = []
ROOMS = ["Main Floor", "Art Studio", "Workshop", "Closet", "Center", 'Go home']
ITEMS = [['Canvas', 'Pallets', 'Table'], ['Bloody counter', 'Pegboard', 'Saw table', ''], []]


def basement(inventory):
    move = ''
    current_room = 'Center'
    item = ''
    while move.strip() != ("M" or "MAIN FLOOR" or "MAIN"):

        # Current Room = Center
        if current_room == 'Center':

            #Move's you out of the room
            print("Nothing to investigate")
            sleep(1.2)
            rooms = [x for x in ROOMS if current_room != x]
            print(f"Where would you like to go?")
            for room in rooms:
                print('[' + room[0] + ']' + room[1:] + ": ", end="")
            move = input("\n\t").upper()
            for i in range(len(rooms)):
                if len(move) > 1:
                    if move == rooms[i][0:len(move)].upper():
                        current_room = rooms[i]
                else:
                    if move == rooms[i][0]:
                        current_room = rooms[i]
            print(f"moving to {current_room}...")
            sleep(1.5)
            print("\n\n")


        # Current Room Art
        elif current_room == 'Art Studio':

            # Input for items
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[0]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()

            # Input checks and assigning
            for i in range(len(ITEMS[0])):
                if len(balls) > 1:
                    if balls == ITEMS[0][i][0:len(balls)].upper():
                        item = ITEMS[0][i]

                else:
                    if balls == ITEMS[0][i][0]:
                        item = ITEMS[0][i]

            # Item interactions and character lines
            if item == 'Canvas':
                print("You examine the picture..")
                sleep(.8)
                for line in Ascii_artr.PALLET.splitlines():
                    print(line)
                    sleep(.086)
                print("What is this??")
                sleep(1.2)
                print("You look closer")
                sleep(1.2)
                print("It's painted with blood..")
                for line in Ascii_artr.DOTS:
                    print(line)
                    sleep(1.9)
                print("You decide to hold onto it.")
                system('cls')
                inventory.append(item)

            elif item == "Pallets":
                print()

            elif item == "Table":
                print()



        # Current Room Work
        elif current_room == 'Workshop':
            item = ''

            # Input for items
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[1]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()

            # Item checks and assigning
            for i in range(len(ITEMS[1])):
                if len(balls) > 1:
                    if balls == ITEMS[1][i][0:len(balls)].upper():
                        item = ITEMS[1][i]
                        break
                else:
                    if balls == ITEMS[1][i][0]:
                        item = ITEMS[1][i]
                        break

            # Item interactions and character lines


        # Current Room Closet
        elif current_room == 'Closet':
            item = ''

            # Input for items
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[2]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()

            # Item checking and assigning
            for i in range(len(ITEMS[2])):
                if len(balls) > 1:
                    if balls == ITEMS[2][i][0:len(balls)].upper():
                        item = ITEMS[2][i]
                        break
                else:
                    if balls == ITEMS[2][i][0]:
                        item = ITEMS[2][i]
                        break

            # Item interactions and character lines



    sleep(1.5)
    return inventory
    #MainFloor.mainfloor()

