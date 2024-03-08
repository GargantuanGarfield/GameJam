# Nicholas Whitton
# 3/7/2024
# The main floor where you search for items.
import basement
import time
import random
import top_floor

selection = ['Basement', 'Upstairs', 'Cabinet', 'Kitchen', 'Check' ]
cabinet_selection = ['[P]owder???', '[T]ape Recorder', '[W]hetstone']
kitchen_selection = ['[ID] Body', '[R]iddle??', 'Egg']
HasKey = False



passnum1 = random.randint(0, 9)


def setting(inventory):
    BASEMENT = False
    global HasKey
    option = input(f'Choose what you want to do {selection}: ').capitalize()
    if 'Working Tape Recorder' in inventory:
        if 'Wheat' in inventory and 'Powdered Sugar' in inventory and 'Egg' in inventory and 'Milk' in inventory:
            print('Great job'), print('.', end=''), time.sleep(1), print('.', end=''), time.sleep(1), print('.'), time.sleep(1)
            print('You go home and make a sweet cake with all of your ingredients.')
            quit()
        else:
            print('Great job'), print('.', end=''), time.sleep(1), print('.', end=''), time.sleep(1), print('.'), time.sleep(1)
            print('You can go home now...')
            quit()
    else:
        pass
    while option not in selection:
        option = input(f'Choose what you want to do {selection}: ').capitalize()
    while not BASEMENT:
        if option == 'Basement' and HasKey == False:
            print('\nThere is a lock with 4 digits here.')
            passcode = input('What is the passcode? ')
            if passcode == str(passnum1) + '298':
                print('You unlocked the basement')
                HasKey = True
            else:
                print('Wrong code.')
            option = input(f'Choose what you want to do {selection}: ').capitalize()

        elif option == 'Basement' and HasKey == True:
            print('Moving to basement')
            BASEMENT = True
            basement.basement(inventory)

        elif option == 'Upstairs':
            inventory += top_floor.main(inventory)

        elif option == 'Cabinet':
            look_for_stuff = input(f'Look in cabinet {cabinet_selection} (Q to leave): ').title()
            if look_for_stuff == 'Q':
                option = input(f'Choose what you want to do {selection}: ').capitalize()

            elif look_for_stuff == ('T' or 'Tape Recorder'):
                print("There's a tape in here...")
                print('This may be useful later.'), time.sleep(1), print('You put the recorder in your bag.')
                inventory.append('Tape Recorder')

            elif look_for_stuff == ('W' or 'Whetstone'):
                print('Why are you looking at the Whetstone???')
                print('.', end=''), time.sleep(1), print('.', end=''), time.sleep(1), print('.'), time.sleep(1)
                print('Wait!'), time.sleep(1)
                print(f'There are the numbers [1:{passnum1}]')

            elif look_for_stuff == ('P' or 'Powder???'):
                print('Hmm this powder is suspicious')
                print('You taste some', end='')
                print('.', end=''), time.sleep(2), print('.', end=''), time.sleep(2), print('.'), time.sleep(2)
                print("Wow! That's some sweet powdered sugar!")
                print('.', end=''), time.sleep(2), print('.', end=''), time.sleep(2), print(' You take some for later'), time.sleep(2)
                inventory.append('Powdered Sugar')


            else:
                print("Can't do that in the cabinet!")

        elif option == 'Kitchen':
            print('In the corner of the room there is a body!')
            look_in_kitchen = input(f'Look in cabinet {kitchen_selection} (Q to leave): ')
            if look_in_kitchen == 'Q':
                option = input(f'Choose what you want to do {selection}: ').capitalize()

            elif look_in_kitchen == ('ID' or 'ID Body'):
                print("Hmm you can't seem to identify the name on the body.")

            elif look_in_kitchen == ('R' or 'Riddle'):
                print('You have 1 MOUTH, and you should LISTEN to me TWICE as much as you are talking. HOW MANY EARS DO YOU HAVE?')
                print('.', end=''), time.sleep(2), print('.', end=''), time.sleep(2), print('.'), time.sleep(2)
                answer = input('How many ears do you have')
                while answer != '2':
                    print("That doesn't seem like the right answer")
                    answer = input('How many ears do you have? ')
                else:
                    print('This may be part of a passcode of some kind [2:2]')


            elif look_in_kitchen == 'Egg':
                print('Egg???'), time.sleep(2)
                print('This may be useful')
                inventory.append('Egg')
        elif option == 'Check':
            print('You have: ')
            for i in inventory:
                print('-'+i)
            print('in your inventory.')
            option = input(f'Choose what you want to do {selection}: ').capitalize()
        else:
            print('Not a valid option!')
            option = input(f'Choose what you want to do {selection}: ').capitalize()
    return inventory



