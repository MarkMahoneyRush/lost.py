from time import sleep
import os

def gameover():
    print("   _____            __  __  ______" )
    print("  / ____|    /\    |  \/  ||  ____|")
    print(" | |  __    /  \   | \  / || |__   ")
    print(" | | |_ |  / /\ \  | |\/| ||  __|  ")
    print(" | |__| | / ____ \ | |  | || |____ ")
    print("  \_____|/_/    \_\|_|  |_||______|")
    print(                                   )
    print(                                   )
    print("   ____ __      __ ______  _____   ")
    print("  / __ \\ \    / /|  ____||  __ \  ")
    print(" | |  | |\ \  / / | |__   | |__) | ")
    print(" | |  | | \ \/ /  |  __|  |  _  /  ")
    print(" | |__| |  \  /   | |____ | | \ \  ")
    print("  \____/    \/    |______||_|  \_\ ")                                
                                       

bag=["drink","protein bar","shoes","pocketknife",]
print("Made By Miniclip")
sleep(2)
print("Presents...")
sleep(2)
print("Lost")
sleep(2)
player=input("choose your character, 1 is boy or 2 is girl?")

if player == ("1"):
    gender=("he")
               
elif player == ("2"):
    gender=("she")
print(gender)
sleep(2)
print(" is walking in the town at night")
sleep(2)
print(gender)
print(" comes across a dark shortcut through the woods")
sleep(2)
choice1=input("1 take the shortcut or 2 take the long way")
while True:
    if choice1 == ("1"):
        print("youre safe")
        break       
    elif choice1 == ("2"):
        gameover()
    
print("they come across courtmill, their home town")
"""
os.system("powershell -c C:S:/MAP FOR GAME.jpeg")
"""
choice2=input("where would you like to go? 1/your house,2/ the shops, 3/ the playground, 4/ the forest, 5/ the river")
while True:
if choice2 == ("1"):
    print("you pick up your bag, here is the items in it")
    print (bag)
    break
if choice2 == ("2"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice2 == ("3"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice2 == ("4"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice2 == ("5"):
    print("you are at the river")
    print ("go home")


choice3=input("where would you like to go? 1/your house,2/ the shops, 3/ the playground, 4/ the forest, 5/ the river")
while True:
if choice3 == ("1"):
    print("you havent forgotten anything")
    
    break
if choice3 == ("2"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice3 == ("3"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice3 == ("4"):
    print("you remember that you left your shoes at home as you were swimming in the river")
if choice3 == ("5"):
    print("you are at the river")
    print ("go home")
