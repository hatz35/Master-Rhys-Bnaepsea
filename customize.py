#===================== CUSTOMIZE =====================
from internal.player import Player
from internal.basic import clear_screen, prompt, wait
from internal.database import all_players

def customize_menu():
    clear_screen()
    print("Add, Remove, Back?")
    p = prompt()
    if p  == "add":
        addplayer()
    elif p == "back":
        from master import main_menu
        main_menu()
    elif p == "remove":
        remove_player()
    else:
        print("Try Again")
        wait(1)
        customize_menu()

def addplayer():
    clear_screen()
    try:
        newname, newrating = input("Enter Name: "), input("Enter Rating: ")
        all_players.append(Player(newname, int(newrating)))
        print("Added")
        wait(1)
        customize_menu()

    except ValueError as err:
        print(err)
        print("Try Again")
        wait(1)
        customize_menu()
