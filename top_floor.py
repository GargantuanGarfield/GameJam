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

HasKeyToBasement = False
inventory = []

def main(HasKeyToBasement, inventory):
    selections = ["[B]edroom", "[O]ffice", "[Ba]throom", "[D]ownstairs"]
    print("You have entered the 2nd floor")
    do_input = (input("What do yo you want to do? Options: go back downstairs, look around: ")).lower()
    if do_input == "go back downstairs":
        print("Going back downstairs...")
        # Call main function from middle floor
        MainFloor.setting()
    while do_input == "look around":
        room_input = input(f"What room do you want to enter? {selections}: ")
        if room_input == "B":
            print("You have entered the bedroom")
        elif room_input == "O":
            print("You have entered the office")
            office_input = input("What would you like to look at? ([C]omputer, [D]esk, [B]ookshelf): ")
            if office_input == "C":
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
                else:
                    for i in f"I chose {computer_choice}. Congrats, you win! Look at the bookshelf...":
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print()
                    print("You find a secret elevator behind the bookshelf!")
            elif office_input == "D":
                pass
            elif office_input == "B":
                print("Try checking the computer...")



        elif room_input == "Ba":
            print("You have entered the bathroom")

        elif room_input == "D":
            print("Going back downstairs...")
            MainFloor.setting()
    return HasKeyToBasement, inventory



main(HasKeyToBasement, inventory)