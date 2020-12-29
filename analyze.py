#===================== ANALYZE =====================
from internal.basic import clear_screen, prompt, wait

import json

#DATABASE MANAGEMENT
def getJson():
    with open('record.json', 'r') as f:
        return json.load(f)

def saveJson(newfile):
    with open('record.json', 'w') as f:
        json.dump(newfile, f, indent = 8)


#FUNCTIONS
def waiter():
    wait(2)
    n = input("Press Enter to Continue")
    analyze_menu()

def listingplayers():
    print("----- All Players -----")
    count = 1
    data = getJson()
    for i, v in data["individuals"].items():
        print(f"[{count}] {i} - {v}")
        count += 1
    waiter()

def top():
    print("----- All Players -----")
    count = 1
    data = getJson()
    x =data["individuals"]
    new_x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
    for i, v in new_x.items():
        print(f"[{count}] {i} - {v}")
        count += 1
    waiter()


#MENU
analyze_text = ('''\n\n~~~~~~~~~~~~ ANALYZE ~~~~~~~~~~~~
    1. Show List             - Press 1
    2. Leaderboard           - Press 2
    3. Back to Menu          - Press 3
''')

def analyze_menu():
    clear_screen()
    print(analyze_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        listingplayers()
    elif p == 2:
        top()
    elif p == 3:
        from master import main_menu
        main_menu()
    else:
        print("Try Again")
        wait(1)
        analyze_menu()
