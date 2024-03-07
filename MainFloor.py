# Nicholas Whitton
# 3/7/2024
# The main floor where you search for items.
inventory = []
selection = ['Basement', 'Upstairs', 'Cabinet', 'Kitchen' ]
cabinet_selection = ['[P]owder???', '[B]loody Knife', '[W]hetstone']
HasKey = False
import time
import random
# import basement


def background():
    """You arrive at the crime scene...
It is a run down house with broken glass and spots of blood everywhere.
You enter the building, try looking for evidence to solve this case.
"""
print(background.__doc__)
passnum1 = random.randint(0,9)


def setting(player):
    global HasKey
    option = input(f'{player}, Choose what you want to do {selection}: ').capitalize()
    while option not in selection:
        option = input(f'Choose what you want to do {selection}: ').capitalize()
    while not HasKey:
        if option == 'Basement' and not HasKey:
            print('\n You dont have the Key for that')
            option = input(f'Choose what you want to do {selection}: ').capitalize()
        elif option == 'Basement' and HasKey == True:
            option = input(f'Choose what you want to do {selection}: ').capitalize()
            pass # will be basement.basement()
        elif option == 'Upstairs':
            option = input(f'Choose what you want to do {selection}: ').capitalize()
            pass  # will be top_floor.basement()
        elif option == 'Cabinet':
            look_for_stuff = input(f'Look in cabinet {cabinet_selection} (Q to leave): ').title()
            if look_for_stuff == 'Q':
                option = input(f'Choose what you want to do {selection}: ').capitalize()
            elif look_for_stuff == ('B' or 'Bloody Knife'):
                print('You look at the dried blood on the knife.')
                print('This may be useful later.'), time.sleep(1), print('You put the knife in your bag.')
                inventory.append('Bloody Knife')

            elif look_for_stuff == ('W' or 'Whetstone'):
                print('Why are you looking at the Whetstone???')
                print('.', end=''), time.sleep(2), print('.', end=''), time.sleep(2), print('.'), time.sleep(2)
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
            HasKey = True
        else:
            print('Not a valid option!')
            option = input(f'Choose what you want to do {selection}: ').capitalize()





