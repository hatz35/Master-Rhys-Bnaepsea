#===================== MATCHES =====================
from internal.player import Player, player_data
from internal.basic import clear_screen, prompt, wait
import json
import random
import math

#DATABASE MANAGEMENT
def getJson():
    with open('record.json', 'r') as f:
        return json.load(f)

def saveJson(newfile):
    with open('record.json', 'w') as f:
        json.dump(newfile, f, indent = 8)


#Functions
def matchfixing(no_of_matches, isSlow):
    print("Tournament Done")
    if isSlow:
        time.sleep(4)


def runT():
    no_of_matches = int(input("Enter Matches Number: "))
    prompt2 = int(input("0 - Slow, 1 - Fast\nPress 1 or 2: "))
    if prompt2 == 0: #slow
        matchfixing(no_of_matches, True)
    if prompt2 == 1: #fast
        matchfixing(no_of_matches, False)
    else:
        print ("Try Again\n\n")
        runT()
    Menu()

def runD():
    p1 = input("Enter First Fighter Name: ")
    p2 = input("Enter Second Fighter Name: ")
    data = getJson()
    #not_working
    #gotta see if these two are in list
    #prefer to learn any
    result = any(p1 in d.values for d in data["individuals"].values())
    result2 = any(p2 in d.values() for d in data.values())
    print(f"Found {p1} {result} and {p2} {result2}")
    prompt2 = int(input("0 - Official, 1 - Unofficial, Enter: "))
    if prompt2 == 0:
        duel(p1, p2, True)
    if prompt2 == 1:
        duel(p1, p2, False)
    else:
        Menu()
    Menu()

#======================================================================
#MENU

matches_text = ('''\n\n~~~~~~~~~~~~ CUSTOMIZE ~~~~~~~~~~~~
    1. Run Tournament             - Press 1
    2. 1v1 Match Fix              - Press 2
    3. Back to Menu               - Press 3
''')

def matches_menu():
    clear_screen()
    print(matches_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        runT()
    elif p == 2:
        runD() #Undone
    elif p == 3:
        from master import main_menu
        main_menu()
    else:
        print("Try Again. Press 1 or 2 or 3 or 4")
        wait(2)
        customize_menu()
