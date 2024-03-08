#
# Gavin Mckenzie
# 3/6/24
# Starter code
from colorama import Fore, Style
import Ascii_artr
from os import system
from time import sleep
import basement
# import MainFloor
# import top_floor
import success_failure

def main():
    inventory = []
    print(f"{Ascii_artr.TITLE_CARED}")
    player = input("Enter your last name: ")
    for line in Ascii_artr.CONNER.splitlines():
        print(line)
        sleep(.086)
    print(f" - Welcome detective {player}, Let's cut to the {Fore.RED}{Style.BRIGHT}CHASE{Style.RESET_ALL}")
    print(f"\t - Detective... We have a problem--")
    input(f"What happened? \n\t").lower()
    print(f"\n{Style.BRIGHT} - What are you talking about? No there's been a string of murders!{Style.RESET_ALL}\
Now is not the time for jokes..\n\tWe found where the killer has been hiding out, so go investigate.")
    print()
    yes = input("Go now?\n\t(y/n): ").lower().strip()
    while yes != 'y':
        print("Try again")
        yes = input("Go now?\n\t(y/n): ").lower().strip()
    print("Wonderful\n")
    system("cls")
    for line in Ascii_artr.DOTS:
        print(line, end="")
        sleep(.8)
    print()
    inventory = basement.basement(inventory)
    #MainFloor.system()
    print("done")


main()