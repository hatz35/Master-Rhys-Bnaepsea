#===================== MATCHES =====================
from internal.team import Team, team_data
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
def check(p, p2 = ""):
    data = getJson()
    result = any(p == d for d in data["teams"])
    if p == p2:
        print ("Error Occured. Both Combatant teams are same")
        wait(1)
        matches_menu()
    if result == False:
        print ("Alphrid by this name doesn't exist.")
        wait(1)
        matches_menu()
    else:
        return

def find_k(team, rating):
    data = getJson()
    matches = (data["teams"][team]["team_data"]["Wins"]
               + data["teams"][team]["team_data"]["Losses"]
               + data["teams"][team]["team_data"]["Draws"])

    if matches <= 30 and rating <= 230:
        k = 40

    elif matches >= 30 and rating <= 240:
        k = 30

    elif matches >= 30 and rating <= 240:
        k = 10

    elif matches <= 30 and rating <= 230:
        k = 25

    print (team, str(k))
    return k

def elo(isDraw, a, b):
    data = getJson()
    if isDraw:
        data["teams"][a]["team_data"]["Draws"] += 1
        data["teams"][b]["team_data"]["Draws"] += 1
        score_a = 0.5
        score_b = 0.5

    else:
        data["teams"][b]["team_data"]["Wins"] += 1
        data["teams"][a]["team_data"]["Losses"] += 1
        score_a = 1
        score_b = 0

    rating_a, rating_b = data["teams"][a]["team_data"]["Rating"], data["teams"][b]["team_data"]["Rating"]
    probability_a = 1/(1 + 10**((rating_b - rating_a)/100))
    probability_b = 1/(1 + 10**((rating_a - rating_b)/100))
    k1 = find_k(a, rating_a)
    k2 = find_k(b, rating_b)
    change1 = int(round(((k1*(score_a - probability_a))/10),1))
    change2 = int(round(((k2*(score_b - probability_b))/10),1))

    print (str(rating_a), " + ", str(change1))
    print (str(rating_b), " + ", str(change2))
    data["teams"][a]["team_data"]["Rating"] += change1
    data["teams"][b]["team_data"]["Rating"] += change2
    wait(4)
    saveJson(data)
    matches_menu()

def submit_duel(p1, p2):
    clear_screen()
    matches_text = (f'''\n\n~~ {p1} VS {p2} ~~
        1. {p1} Won
        2. {p2} Won
        3. Draw
        4. Back
    ''')
    print(matches_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        elo(False, p1, p2)
    elif p == 2:
        elo(False, p2, p1)
    elif p == 3:
        elo(True, p1, p2)
    elif p == 4:
        matches_menu()
    else:
        print("Try Again. Press 1 or 2 or 3 or 4")
        wait(2)
        submit_duel()

def sub_mat():
    p1 = input("Enter First Alphrid: ")
    check(p1)
    p2 = input("Enter Second Alphrid: ")
    check(p2, p1)
    print("\nPreparing Match...")
    wait(1)
    submit_duel(p1, p2)
    matches_menu()


def gen_mat():
    data = getJson()
    all_teams = [i for i, _ in data["teams"].items()]
    k = random.sample(all_teams, 2)
    submit_duel(k[0], k[1])
#======================================================================
#MENU

matches_text = ('''\n\n~~~~~~~~~~~~ CUSTOMIZE ~~~~~~~~~~~~
    1. Submit Match               - Press 1
    2. Generate Match             - Press 2
    3. Back to Menu               - Press 3
''')

def matches_menu():
    clear_screen()
    print(matches_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        sub_mat()
    elif p == 2:
        gen_mat()
    elif p == 3:
        from master import main_menu
        main_menu()
    else:
        print("Try Again. Press 1 or 2 or 3 or 4")
        wait(2)
        customize_menu()
