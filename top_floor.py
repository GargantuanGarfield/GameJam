#
# Vir Patel
# 3/7/2024
# The top floor of the house
#

#import basement
import MainFloor
import random
import sys
import time
import Ascii_artr
from colorama import Fore, Style

HasKeyToBasement = False
inventory = []

def main(HasKeyToBasement, inventory):
    selections = ["[B]edroom", "[O]ffice", "[Ba]throom", "[D]ownstairs"]
    print("You have entered the 2nd floor")
    do_input = (input("What do yo you want to do? Options: go back downstairs, look around: ")).lower()
    if do_input == "go back downstairs":
        print("Going back downstairs...")
        # Call main function from middle floor
        MainFloor.setting(inventory)
    while do_input == "look around":
        room_input = input(f"What room do you want to enter? {selections}: ")
        if room_input == "B":
            print("You have entered the bedroom")
            look_at_input = input("What do you want to look at? (Mirror, under bed, dresser): ")
            if look_at_input.lower() == "mirror":
                print(Ascii_artr.YOU)
        elif room_input == "O":
            print("You have entered the office")
            office_input = input("What would you like to look at? ([C]omputer, [D]esk, [B]ookshelf): ")
            if office_input.lower() == "c":
                # Credit to https://youtu.be/rGMvZuPebzA?si=O9niY98kbFp6GnFX
                computer_says = "Play me in rock paper scissors"
                for i in computer_says:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.1)
                print()
                rps_list = ['rock', 'paper', 'scissors']
                computer_choice = rps_list[random.randint(0,2)]
                rps_input = (input("Rock, paper, or scissors?: ")).lower()
                while (rps_input.lower() == 'rock' and computer_choice == 'paper') or (rps_input == 'paper' and computer_choice == 'scissors') or (rps_input == 'scissors' and computer_choice == 'rock') or (rps_input == computer_choice):
                    for i in f"I choose {computer_choice}. Try again\n":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    rps_input = (input("Rock, paper, or scissors?: ")).lower()
                # Unused code hehehehaw
                '''
                if rps_input == 'rock' and computer_choice == 'paper':
                    for i in f"I choose {computer_choice}. I win, try again":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                elif rps_input == 'paper' and computer_choice == 'scissors':
                    for i in f"I choose {computer_choice}. I win, try again":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                elif rps_input == 'scissors' and computer_choice == 'rock':
                    for i in f"I choose {computer_choice}. I win, try again":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                elif rps_input == computer_choice:
                    for i in f"I choose {computer_choice}. Tie, try again":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                '''
                for i in f"I chose {computer_choice}. Congrats, you win! Look at the bookshelf...":
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.1)
                print()
                print("You find a secret room behind the bookshelf!")
                print("There's a code written in blood on the wall!")
                print(f"{Fore.RED}{Style.BRIGHT}98{Style.RESET_ALL}")

            elif office_input.lower() == "d":
                pass
            elif office_input.lower() == "b":
                print("Try checking the computer...")



        elif room_input == "Ba":
            print("You have entered the bathroom, you see a bar of soap and clean yourself up")
            # Add a mirror that displays ASCII Art or smthn else like soap
            bathroom_input = input("What do you want to look at? (Mirror, soap, toilet): ")
            if bathroom_input.lower() == "mirror":
                print(Ascii_artr.JOSH)
            elif bathroom_input.lower() == "soap":
                print("*Takes bite of soap*")
                print("Yummers, I will keep this for later")
                print("Soap added to inventory")
                inventory.append("soap")
            elif bathroom_input.lower() == "toilet":
                print(Ascii_artr.TOILET)


        elif room_input == "D":
            print("Going back downstairs...")
            MainFloor.setting(inventory)

    do_input = (input("What do yo you want to do? Options: go back downstairs, look around: ")).lower()
    if do_input == "go back downstairs":
        print("Going back downstairs...")
        return HasKeyToBasement, inventory
    else:
        MainFloor.setting(inventory)



main(HasKeyToBasement, inventory)