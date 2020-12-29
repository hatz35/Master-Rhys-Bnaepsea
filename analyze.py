#===================== ANALYZE =====================
from internal.basic import clear_screen, prompt, wait
from internal.database import all_players


def waiter():
    wait(2)
    n = input("Press Enter to Continue")
    analyze_menu()

def listingplayers():
    print("----- All Players -----")
    count = 1
    for i in all_players:
        print(f"[{count}] {i.name} - {i.rating}")
        count += 1
    waiter()

def top():
    print("----- All Players -----")
    count = 1
    for i in all_players:
        print(f"[{count}] {i.name} - {i.rating}")
        count += 1
    waiter()

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
