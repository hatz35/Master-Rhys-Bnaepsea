#===================== CUSTOMIZE =====================
from internal.player import Player
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
def add_to_json(newname, newrating):
    data = getJson()
    for ind in data["individuals"]:
        if ind == newname:
            print(f"{newname} is alreaedy there)")
            wait(1)
            customize_menu()

    data["individuals"][newname] = newrating
    saveJson(data)
    print(f"{newname} has been successfully added.")
    wait(1)
    customize_menu()

def remove_from_json(name):
    data = getJson()
    for ind in data["individuals"]:
        if ind == name:
            del data["individuals"][name]
            print(f"{name} has been removed")
            wait(1)
            saveJson(data)
            customize_menu()
    print(f"{name} not found")
    wait(1)
    customize_menu()

def delete_db():
    data = getJson()
    data["individuals"] = {}
    print(f"Database Cleared")
    wait(1)
    saveJson(data)
    customize_menu()

#MENU

customize_text = ('''\n\n~~~~~~~~~~~~ CUSTOMIZE ~~~~~~~~~~~~
    1. Add Individual             - Press 1
    2. Remove Individual          - Press 2
    3. Back to Menu               - Press 3
    4. Delete Database <WARNING>  - Press 4
''')

def customize_menu():
    clear_screen()
    print(customize_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        add_player()
    elif p == 2:
        remove_player()
    elif p == 3:
        from master import main_menu
        main_menu()
    elif p == 4:
        delete_players()
    else:
        print("Try Again. Press 1 or 2 or 3 or 4")
        wait(2)
        customize_menu()

def add_player():
    clear_screen()
    try:
        newname, newrating = input("Enter Name: "), input("Enter Rating: ")
        add_to_json(newname, newrating)
        customize_menu()

    except ValueError as err:
        print(err)
        print("Try Again")
        wait(1)
        customize_menu()

def remove_player():
    clear_screen()
    name = input("Find individual by their name - ")
    remove_from_json(name)

def delete_players():
    clear_screen()
    delete_db()
