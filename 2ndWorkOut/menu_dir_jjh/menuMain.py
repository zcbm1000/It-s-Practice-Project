from menu import showMenu
from exitMenu import exitMenu

while True:

    choice = showMenu()

    if choice == 0:
        if exitMenu():
            break

        else:
            continue