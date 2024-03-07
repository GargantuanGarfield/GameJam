#
# Gavin McKenzie
# 3/7/24
# Code for the Basement floor of the game
# import MainFloor
from time import sleep
from os import system
import Ascii_artr

ROOMS = ["Main Floor", "Art Studio", "Workshop", "Closet", "Center", 'Inventory']
ITEMS = [['Canvas', 'Palettes', 'Table', 'Inventory', 'Leave'], ['Bloody counter', 'Pegboard', 'Saw table', 'Inventory',
         'Leave'], ['Top shelf', 'Inventory', 'Leave']]


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
            if current_room == 'Inventory':
                pass
            else:
                print(f"moving to {current_room}...")
                sleep(1.5)
            print("\n\n")


        # Current Room Art
        elif current_room == 'Art Studio':
            # Input for items
            print("\nWhat would you like to investigate?\n\t(enter 'L' to leave)")
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
            if item == 'Leave':
                current_room = 'Center'
                print("Leaving..")
                sleep(1.5)
            elif item == "Palettes":
                print("You check the art Palettes...")
                sleep(1.2)
                for line in Ascii_artr.PALLET.splitlines():
                    print(line)
                    sleep(.086)
                print("You don't find anything of note..")
                sleep(1.8)
                print("Back to searching")
                ITEMS[0].remove(item)


            elif item == "Table":
                for line in Ascii_artr.TABLE.splitlines():
                    print(line)
                    sleep(.086)
                print("Doesn't look like anything too important")
                print("\t.. strange choice of table")
                for line in Ascii_artr.DOTS[0:6]:
                    print(line, end="\t")
                    sleep(1.5)
                print("\n\tWAIT")
                print("Theres something underneath it")
                sleep(1.2)
                print("You found a battery!")
                sleep(1.6)
                print("You put it in your pocket")
                system('cls')
                inventory.append('Battery')
                ITEMS[0].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                for thing in inventory:
                    if thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Battery" or "Key" or "Tape Recorder"):
                        print(' - ' + thing + ' [KEY]')
                    else:
                        print(' - ' + thing)

            elif item == 'Canvas':
                print("You examine the picture..")
                sleep(.8)
                for line in Ascii_artr.CANVAS.splitlines():
                    print(line)
                    sleep(.086)
                print("What is this??")
                sleep(1.2)
                print("You look closer")
                sleep(1.2)
                print("It's painted with blood..")
                for line in Ascii_artr.DOTS:
                    print(line, end="\t")
                    sleep(1.9)
                print("\nYou decide to hold onto it.")
                sleep(1.2)
                print("You've acquired 'Strange Painting'")
                system('cls')
                inventory.append('Strange Painting')
                ITEMS[0].remove(item)



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
            if item == 'Leave':
                current_room = 'Center'
                print("Leaving..")
                sleep(1.5)

            elif item == "Pallets":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[1].remove(item)

            elif item == "Pallets":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[1].remove(item)

            elif item == "Paletts":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[1].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                for thing in inventory:
                    if thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Battery" or "Key" or "Tape Recorder"):
                        print(' - ' + thing + ' [KEY]')
                    else:
                        print(' - ' + thing)

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
            if item == 'Leave':
                current_room = 'Center'
                print("Leaving..")
                sleep(1.5)

            elif item == "Pallets":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[2].remove(item)

            elif item == "Pallets":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[2].remove(item)

            elif item == "Pallets":
                print()
                for line in Ascii_artr.art.splitlines():
                    print(line)
                    sleep(.086)
                inventory.append(item)
                ITEMS[2].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                for thing in inventory:
                    if thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Battery" or "Key" or "Tape Recorder"):
                        print(' - ' + thing + ' [KEY]')
                    else:
                        print(' - ' + thing)

        elif current_room == 'Inventory':
            system('cls')
            print("You check your pockets")
            for thing in inventory:
                if len(inventory) == 0:
                    print("Nothing is there")
                    sleep(1.2)
                elif thing == 'Strange Painting':
                    print(' - ' + thing + ' [VERY IMPORTANT]')
                    sleep(.7)
                elif thing == ("Battery" or "Key" or "Tape Recorder"):
                    print(' - ' + thing + ' [KEY]')
                    sleep(.7)
                else:
                    print(' - ' + thing)
                    sleep(.7)
            print("\n\n")
            sleep(2)
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


    sleep(1.5)
    return inventory

