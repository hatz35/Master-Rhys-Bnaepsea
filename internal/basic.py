import time

def clear_screen():
    print("\033[H\033[J")

def prompt(isnum = False, text = ""):
    if isnum:
        return int(input(text))
    else:
        return input(text).lower().strip()

def wait(n):
    time.sleep(n)
