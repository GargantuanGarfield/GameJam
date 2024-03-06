#
# Gavin Mckenzie
# 3/6/24
# Starter code
from colorama import Fore, Back, Style
import Ascii_artr

print(f"{Ascii_artr.TITLE_CARED}")
player = input("Enter your name: ")
print(f"Welcome detective {player}, Let's cut to the {Fore.RED}{Style.BRIGHT}CHASE{Style.RESET_ALL}")
print(f"\tDetective... Something happened,")

list_of_crimes = ["the murder?", "the arson?", "the drug house?"]
crime = input(f"WHat happened {list_of_crimes}?\n\t").lower()
while crime not in list_of_crimes:
    print("That didn't happen...")
    crime = input(f"WHat happened {list_of_crimes}?\n\t")

print("I guess you've already heard the bad news, get down to the crime house and investigate..")
yes = input("Go now? (y/n) ").lower()
if yes == 'n':
    print("Too bad, you're going")

