import random

'''

This is the main class for the python game.

For now, all code will be here, until we get to classes, then we can start divying up code among files. 



'''

#Global veriable to hold the dungeon map
global dungeon

'''
MAIN FUNCTION
'''
def main():
    menu()

'''
NAME: menu

Desc: Responsible for getting hte player input for the game

PARAM: NA

RETURN: NA
'''
def menu():
    return


'''
NAME: startGame

Desc: Responsible for controlling the start of the game including setup, player initialization and
      map creation

PARAM: NA

RETURN: NA
'''
def startGame():
    generate_dungeon()

'''
NAME: generate_dungeon

Desc: Responsible for creating and setting up the dungeon, will create the map, then populate it with significant locations
      such as items, player start, enemy locations and exit location
'''
def generate_dungeon():
    global dungeon
    dungeon = []




#call main
main()