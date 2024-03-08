#
# Gavin McKenzie
# 3/7/24
# success or failure function
import random as r
import colorama as c
from time import sleep
def success_fail():
    count = 0
    while count < 5:
        roll = r.randint(0,10)
        print("Commencing Sleight of Hand check...")
        if roll == 0:
            print(roll)
            print("CRITICAL FAILURE")
            sleep(1.2)
            print("The key is broken...")
            sleep(1.8)
            print(f"{c.Style.BRIGHT}CR-CRACK{c.Style.RESET_ALL}")
            sleep(1.8)
            print("But you kick it down")
            sleep(1.2)
            print("The door is open")
            return True
        elif roll < 5:
            print(roll)
            sleep(1.2)
            print("Faulure..")
            sleep(1.2)
            print("You dropped the key")
            sleep(1.2)
            print("...")
            sleep(2)
            print("You picked it back up")
            sleep(1.2)
            return False
        else:
            print(roll)
            print('SUCCESS!!!')
            sleep(1.2)
            print("The door opens")
            return True


