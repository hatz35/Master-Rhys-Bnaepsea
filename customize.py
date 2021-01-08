#===================== CUSTOMIZE =====================
from internal.team import Team, team_data
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

def add_to_json(team_data):
    data = getJson()
    newteam = Team(team_data)
    #howmany
    count=1
    for i in data["teams"].items():
        count += 1
    data["teams"][f"{newteam.team_data['Epithet']}"] = newteam.__dict__
    saveJson(data)
    print(f"{newteam.team_data['Epithet']} has been successfully added.")
    wait(1)
    #update_entry()
    customize_menu()


def remove_from_json(name):
    data = getJson()
    for ind, val in data["teams"].items():
        if val["team_data"]["Epithet"] == name:
            del data["teams"][ind]
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
    data["teams"] = {}
    print(f"Database Cleared")
    wait(1)
    saveJson(data)
    customize_menu()

#MENU

customize_text = ('''\n\n~~~~~~~~~~~~ CUSTOMIZE ~~~~~~~~~~~~
    1. Add Alphrid                - Press 1
    2. Remove Alphrid             - Press 2
    3. Back to Menu               - Press 3
    4. Delete Database <WARNING>  - Press 4
''')

def customize_menu():
    clear_screen()
    print(customize_text)
    p = prompt(True, "Press a Number: ")
    if p  == 1:
        add_team()
    elif p == 2:
        remove_team()
    elif p == 3:
        from master import main_menu
        main_menu()
    elif p == 4:
        warn = input("Are you sure? Type 'Rhys' to Delete Everything")
        if warn.lower() == "rhys":
            delete_teams()
        else:
            wait(2)
            customize_menu()
    else:
        print("Try Again. Press 1 or 2 or 3 or 4")
        wait(2)
        customize_menu()

def clear_stuff():
    for  _, j in team_data.items():
        j == None


def add_team():
    clear_screen()
    try:
        for i in team_data:
            if i == "Epithet":
                team_data[i] = input(f"Enter {i}: ")
                data = getJson()
                for entry, val in data["teams"].items():
                    old = val["team_data"]["Epithet"]
                    new = team_data[i]
                    if new == old:
                        print(f"{new} is alreaedy there")
                        wait(1)
            elif i == "Members":
                for j in range(1, int(team_data["Size"])+1):
                    team_data["Members"].append(input(f"Enter Member {j}: "))
            elif i == "Description":
                team_data[i] = input(f"Enter {i}: ")
            else:
                team_data[i] = int(input(f"Enter {i}: "))

        add_to_json(team_data)
        clear_stuff()
        customize_menu()

    except ValueError as err:
        print(err)
        print("Try Again")
        wait(1)
        clear_stuff()
        customize_menu()

def remove_team():
    clear_screen()
    name = input("Find Alphrid by their name - ")
    remove_from_json(name)

def delete_teams():
    clear_screen()
    delete_db()
