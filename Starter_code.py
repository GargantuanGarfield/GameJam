#
# Gavin Mckenzie
# 3/6/24
# Starter code
from colorama import Fore, Back, Style
import Ascii_artr

print(f"{Ascii_artr.TITLE_CARED}")
player = input("Enter your name: ")
print(Ascii_artr.CONNER)
print(f"Welcome detective {player}, Let's cut to the {Fore.RED}{Style.BRIGHT}CHASE{Style.RESET_ALL}")
print(f"\tDetective... We have a problem--")
list_of_crimes = ["the murder?", "the robbery?", "the drug house?"]
crime = input(f"What happened {list_of_crimes}?\n\t").lower()
while crime not in list_of_crimes:
    print("That didn't happen...")
    crime = input(f"WHat happened {list_of_crimes}?\n\t")
print("I guess you've already heard the bad news, get down to the crime scene and investigate..")
yes = input("Go now? (y/n) ").lower().strip()
if yes == 'n':
    print("Didn't ask")
