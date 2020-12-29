#===================== ANALYZE =====================
from internal.basic import clear_screen, prompt, wait
from internal.database import all_players

def listingplayers():
    print("----- All Players -----")
    count = 1
    for i in all_players:
        print(f"[{count}] {i.name} - {i.rating}")
        count += 1

def top():
    print("----- All Players -----")
    count = 1
    for i in all_players:
        print(f"[{count}] {i.name} - {i.rating}")
        count += 1

def analyze_menu():
    clear_screen()
    print("List, Top, Back?")
    p = prompt()
    if p  == "list":
        listingplayers()
    elif p == "back":
        from master import main_menu
        main_menu()
    elif p == "top":
        top()
    else:
        print("Try Again")
        wait(1)
        analyze_menu()
