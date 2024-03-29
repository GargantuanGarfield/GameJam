#
# Gavin McKenzie
# 3/7/24
# Code for the Basement floor of the game
# import MainFloor
from time import sleep
import Ascii_artr
import MainFloor

ROOMS = ["Main Floor", "Art Studio", "Workshop", "Closet", "Center", 'Inventory']
ITEMS = [['Canvas', 'Palettes', 'Table', 'Inventory', 'Leave'], ['Bloody Counter', 'Pegboard', 'Saw Table', 'Inventory',
         'Leave'], ['Top shelf', 'Strange bag', 'Inventory', 'Leave']]


def basement(inventory):
    move = ''
    current_room = 'Center'
    item = ''
    story = 0
    while move.strip() != ("M" or "MAIN FLOOR" or "MAIN"):

        # Checks for all appropriate key items
        if 'Blue AA Battery' in inventory and 'Tape Recorder' in inventory and 'Red AA Battery' in inventory:
            print("Oh?", end="")
            sleep(.8)
            print("Looks like you have enough batteries for the tape recorder..")
            sleep(1.7)
            print("You have acquired 'Working Tape Recorder'")
            inventory.remove('Red AA Battery')
            inventory.remove('Blue AA Battery')
            inventory.remove('Tape Recorder')
            inventory.append('Working Tape Recorder')
            print('Go back to main floor, and check your inventory.')

        # Current Room Center
        elif current_room == 'Center':
            #Move's you out of the room
            print("Nothing to investigate")
            sleep(1.7)
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
                sleep(1.7)
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
                    sleep(.25)
                print("\n\tWAIT")
                print("Theres something underneath it")
                sleep(1.7)
                print("You found a battery!")
                sleep(1.6)
                print("You put it in your pocket")
                inventory.append('Red AA Battery')
                ITEMS[0].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                sleep(.8)
                for thing in inventory:
                    if len(inventory) == 0:
                        sleep(2)
                        print("Nothing is there")
                        sleep(1.7)
                    elif thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Blue AA Battery" or "Red AA Battery" or "Key" or "Tape Recorder"):
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
                sleep(1.7)
                print("You look closer")
                sleep(1.7)
                print("It's painted with blood..")
                for line in Ascii_artr.DOTS:
                    print(line, end="\t")
                    sleep(.25)
                print("\nYou decide to hold onto it.")
                sleep(1.7)
                print("You've acquired 'Strange Painting'")
                inventory.append('Strange Painting')
                ITEMS[0].remove(item)



        # Current Room Work
        elif current_room == "Workshop":
            item = ''

            #Story lines
            while story < 1:
                print("This..", end="")
                sleep(.9)
                print("Isn't a workshop")
                sleep(1.5)
                print("This place was a butcher shop...")
                for i in Ascii_artr.DOTS[0:4]:
                    print(i, end="\t")
                    sleep(.25)
                print("\nYou throw up in the corner")
                sleep(2)
                print("Well, back to work")
                sleep(1.7)
                story += 1

            # Input for items
            print("\nWhat would you like to investigate?\n\t(enter 'L' to leave)")
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

            elif item == "Bloody Counter":
                print("Ugh, this is gross")
                sleep(.8)
                for line in Ascii_artr.COUNTER.splitlines():
                    print(line)
                    sleep(.086)
                print("You examine the table..")
                sleep(1.7)
                print("The blood seems to be a solution made from many people", end="")
                for i in range(2):
                    print(" . ", end="")
                    sleep(.86)
                print("\nNot worth collecting")
                sleep(1.7)
                print("You start to feel sick again")
                sleep(1.7)
                print("Let's keep looking")
                sleep(1.7)
                ITEMS[1].remove(item)

            elif item == "Pegboard":
                print("Looks like it's got the tools the killer used.")
                sleep(.8)
                for line in Ascii_artr.BOARD.splitlines():
                    print(line)
                    sleep(.086)
                print("Most of the items are wiped clean")
                sleep(.8)
                print("looks like theres a knife on the floor that was skipped")
                sleep(1.7)
                print("Must not be loved..")
                sleep(.8)
                print("Or loved a bit too much")
                sleep(1.7)
                print("Probably good evidence")
                sleep(1.7)
                print("You've acquired the 'Bloody Knife'")
                sleep(1.7)
                print("These weapons are making me uneasy")
                sleep(.9)
                inventory.append('Bloody Knife')
                ITEMS[1].remove(item)

            elif item == "Saw Table":
                print("This looks interesting..")
                sleep(.8)
                for line in Ascii_artr.SAW.splitlines():
                    print(line)
                    sleep(.086)
                print("The blade is rusted and red")
                sleep(1.7)
                print("looks like theres something beside it though..")
                sleep(1.8)
                print("You've acquired a 'Blue AA Battery'")
                inventory.append('Blue AA Battery')
                ITEMS[1].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                for thing in inventory:
                    if len(inventory) == 0:
                        sleep(2)
                        print("Nothing is there")
                        sleep(1.7)
                    elif thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Blue AA Battery" or "Red AA Battery" or "Key" or "Tape Recorder"):
                        print(' - ' + thing + ' [KEY]')
                    else:
                        print(' - ' + thing)

        # Current Room Closet
        elif current_room == 'Closet':
            item = ''

            # Input for items
            print("\nWhat would you like to investigate?\n\t(enter 'L' to leave)")
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

            elif item == "Top shelf":
                for line in Ascii_artr.SHELF.splitlines():
                    print(line)
                    sleep(.086)
                print("You reach up to the top shelf of the cabinet...")
                sleep(2)
                print("You can't reach")
                for i in Ascii_artr.DOTS:
                    print(i, end="")
                    sleep(1.4)
                print("\nYou step away in shame")
                ITEMS[2].remove(item)

            elif item == "Strange bag":
                print("You pull out the bag from the closet..")
                sleep(1.7)
                print("The bag is too heavy to be anything normal")
                for line in Ascii_artr.BAG.splitlines():
                    print(line)
                    sleep(.086)
                sleep(2)
                print("I don't even want to know")
                sleep(1.5)
                print("The bag falls and rips, and a severed foot falls out...")
                sleep(2)
                print(". . . . .")
                sleep(4)
                print("I guess I need to take this..")
                sleep(1.3)
                print("So disgusting")
                print("You have acquired 'Severed Foot'!")
                sleep(2)
                print("You throw up again")
                sleep(2)
                print("There goes my lunch.")
                inventory.append('Severed Foot')
                ITEMS[2].remove(item)

            elif item == 'Inventory':
                print("You check your pockets")
                for thing in inventory:
                    if len(inventory) == 0:
                        sleep(2)
                        print("Nothing is there")
                        sleep(1.7)
                    elif thing == 'Strange Painting':
                        print(' - ' + thing + ' [VERY IMPORTANT]')
                    elif thing == ("Blue AA Battery" or "Red AA Battery" or "Key" or "Tape Recorder"):
                        print(' - ' + thing + ' [KEY]')
                    else:
                        print(' - ' + thing)

        elif current_room == 'Inventory':
            print("You check your pockets")
            for thing in inventory:
                if len(inventory) == 0:
                    sleep(2)
                    print("Nothing is there")
                    sleep(1.7)
                elif thing == 'Strange Painting':
                    print(' - ' + thing + ' [VERY IMPORTANT]')
                    sleep(.7)
                elif thing == ("Blue AA Battery" or "Red AA Battery" or "Key" or "Tape Recorder"):
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
    MainFloor.setting(inventory)