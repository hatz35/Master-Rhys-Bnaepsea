#===================== CUSTOMIZE =====================
from internal.player import Player, player_data
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

#not_working
def update_entry():
    data = getJson()
    count=1
    for i in data["individuals"].items():
        data["individuals"][f"Entry#{count}"] = data["individuals"].pop(i)
        count += 1
    saveJson(data)


def add_to_json(player_data):
    data = getJson()
    newplayer = Player(player_data)
    #howmany
    count=1
    for i in data["individuals"].items():
        count += 1
    data["individuals"][f"Entry#{count}"] = newplayer.__dict__
    saveJson(data)
    print(f"{newplayer.player_data['username']} has been successfully added.")
    wait(1)
    #update_entry()
    customize_menu()


def remove_from_json(name):
    data = getJson()
    for ind, val in data["individuals"].items():
        if val["player_data"]["username"] == name:
            del data["individuals"][ind]
            print(f"{name} has been removed")
            wait(1)
            saveJson(data)
            customize_menu()
    print(f"{name} not found")
    wait(1)
    #update_entry()
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
        for i in player_data:
            player_data[i] = input(f"Enter {i}: ")
            if i == "username":
                data = getJson()
                for entry, val in data["individuals"].items():
                    old = val["player_data"]["username"]
                    new = player_data[i]
                    if new == old:
                        print(f"{new} is alreaedy there")
                        wait(1)
                        customize_menu()

        add_to_json(player_data)
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
