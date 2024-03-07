#
# Gavin McKenzie
# 3/7/24
# Code for the Basement floor of the game
# import MainFloor
from time import sleep

INVENTORY = []
ROOMS = ["Main Floor", "Art Studio", "Workshop", "Closet", "Center"]
ITEMS = [['Canvas', 'Pallets', 'Under table'], [], []]
HAS_KEY = True
SWITCH_ACTIVE = True

def basement(inventory):
    move = ''
    current_room = 'Center'
    item = ''
    while move.strip() != ("M" or "MAIN FLOOR" or "MAIN"):

        #Current Room = Center
        if current_room == 'Center':
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


        #Current Room Art
        elif current_room == 'Art Studio':
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[0]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()
            for i in range(len(ITEMS[0])):
                if len(balls) > 1:
                    if balls == ITEMS[0][i][0:len(balls)].upper():
                        print('Balls work')
                else:
                    if balls == ITEMS[0][i][0]:
                        print("balls solo")


        # Current Room Work
        elif current_room == 'Workshop':
            item = ''

            #Input for items
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[1]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()

            #Item checks and setting
            for i in range(len(ITEMS[1])):
                if len(balls) > 1:
                    if balls == ITEMS[1][i][0:len(balls)].upper():
                        item = ITEMS[2][i]
                        break
                else:
                    if balls == ITEMS[1][i][0]:
                        item = ITEMS[2][i]
                        break

        # Current Room Closet
        elif current_room == 'Closet':
            item = ''
            #Input for items
            print("What would you like to investigate?\n\t(enter 'L' to leave)")
            for i in ITEMS[2]:
                print('[' + i[0] + ']' + i[1:] + ": ", end="")
            balls = input(f"\n\t").upper()

            #item checking and setting
            for i in range(len(ITEMS[2])):
                if len(balls) > 1:
                    if balls == ITEMS[2][i][0:len(balls)].upper():
                        item = ITEMS[2][i]
                        break
                else:
                    if balls == ITEMS[2][i][0]:
                        item = ITEMS[2][i]
                        break
    print("Moving to Main Floor...")
    sleep(1.5)
    return inventory
    #MainFloor.mainfloor()

basement(INVENTORY)