#
# Gavin Mckenzie
# 3/6/24
# Starter code
from colorama import Fore, Style
import Ascii_artr
from playsound import playsound

print(f"{Ascii_artr.TITLE_CARED}")
playsound('whistle.mp3')
player = input("Enter your name: ")
print(Ascii_artr.CONNER)
print(f"Welcome detective {player}, Let's cut to the {Fore.RED}{Style.BRIGHT}CHASE{Style.RESET_ALL}")

print(f"\tDetective... Something happened,")
list_of_crimes = ["the murder?", "the robbery?", "the drug house?"]
crime = input(f"WHat happened {list_of_crimes}?\n\t").lower()
while crime not in list_of_crimes:
    print("That didn't happen...")
    crime = input(f"WHat happened {list_of_crimes}?\n\t")

print(f"\tDetective... We have a problem--")
crime = input("What happened?\n\t")
print("I guess you've already heard the bad news, get down to the crime scene and investigate..")
yes = input("Go now? (y/n) ").lower().strip()
if yes == 'n':
    print("Didn't ask")

if crime == "the murder?":
    pass
elif crime == "the robbery?":
    pass
elif crime == "the drug house?":
    pass