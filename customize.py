#===================== CUSTOMIZE =====================
from internal.player import Player
from internal.basic import clear_screen, prompt, wait
from internal.database import all_players, add_to_json

customize_text = ('''\n\n~~~~~~~~~~~~ CUSTOMIZE ~~~~~~~~~~~~
    1. Add Individual             - Press 1
    2. Remove Individual          - Press 2
    3. Back to Menu               - Press 3
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
    else:
        print("Try Again")
        wait(1)
        customize_menu()

def add_player():
    clear_screen()
    try:
        newname, newrating = input("Enter Name: "), input("Enter Rating: ")
        add_to_json(newname, newrating)
        print(f"{newname} has been successfully added.")
        wait(1)
        customize_menu()

    except ValueError as err:
        print(err)
        print("Try Again")
        wait(1)
        customize_menu()

def remove_player():
    clear_screen()
    newname = input("Find individual by their name - ")
    for i in all_players:
        if newname == i.name:
            print("Found One")
        else:
            print(f"Couldn't find {newname}. Maybe try again?")
            wait(2)
            customize_menu()
