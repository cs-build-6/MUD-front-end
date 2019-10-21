import sys
import time
import random
import cmd
import os

screen_width = 150

class player:
    def __init__(self):
        self.name = ""
        self.location = "Starting Point"
        self.game_over = False

myPlayer = player()

def menu_selections():

    option = input ("> ")

    if option.lower()== ("play"):
        setup_game()
    
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ["play", "quit"]:
        print("Please enter a valid command.")

        option = input ("> ")

        if option.lower()== ("play"):
            setup_game()
    
        elif option.lower() == ("quit"):
            sys.exit()

def menu():
    os.system("clear")
    print ("welcome To The CS22 Build 6 MUD")
    print ("-Play-")
    print ("-Quit-")
    menu_selections()





roomDescription = ""
SOLVED = False
roomName = ""
treasureReveal = ""
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"




solved_rooms = {"a1": False, "a2": False, "a3": False, "a4": False, "a5": False, "a6": False, "a7": False, "a8": False, "a9": False, "a10": False,
                "b1": False, "b2": False, "b3": False, "b4": False, "b5": False, "b6": False, "b7": False, "b8": False, "b9": False, "b10": False,
                "c1": False, "c2": False, "c3": False, "c4": False, "c5": False, "c6": False, "c7": False, "c8": False, "c9": False, "c10": False,
                "d1": False, "d2": False, "d3": False, "d4": False, "d5": False, "d6": False, "d7": False, "d8": False, "d9": False, "d10": False,
                "e1": False, "e2": False, "e3": False, "e4": False, "e5": False, "e6": False, "e7": False, "e8": False, "e9": False, "e10": False,
                "f1": False, "f2": False, "f3": False, "f4": False, "f5": False, "f6": False, "f7": False, "f8": False, "f9": False, "f10": False,
                "g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False, "g7": False, "g8": False, "g9": False, "g10": False,
                "h1": False, "h2": False, "h3": False, "h4": False, "h5": False, "h6": False, "h7": False, "h8": False, "h9": False, "h10": False,
                "i1": False, "i2": False, "i3": False, "i4": False, "i5": False, "i6": False, "i7": False, "i8": False, "i9": False, "i10": False,
                "j1": False, "j2": False, "j3": False, "j4": False, "j5": False, "j6": False, "j7": False, "j8": False, "j9": False, "j10": False,               
               }



roomMap = { 
    "a6": {    
       roomName: "Entrace",
       roomDescription: "This is the start of you jorney",
       treasureReveal: "There is no item in this room",
       UP: "",
       SOLVED: False,
       DOWN: "b6",
       LEFT:"a5",
       RIGHT: "a7",
    },
}



def print_location():
    print ('\n' + myPlayer.location)
    print ('\n' + roomMap[myPlayer.position][roomDescription])



def prompt():
    print("What Would You Like To DO?") 
    action = input ("> ")
    valid_input = ["move", "walk", "quit", "reveal"]
    while action.lower() not in valid_input:
        print ("Invalid Input, please try again.\n")
        action = input ("> ")
    
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "walk"]:
        player_move(action.lower())

    elif action.loewr() in ["reveal"]:
        player_reveal(action.lower())


def player_move(myAction):
    whereTo = "where Do You Want To Go?"
    dest = input(whereTo)
    if dest in ["up", "north"]:
        destination = roomMap[myPlayer.location][UP]
        movement_setup(dest)
    elif dest in ["down", "south"]:
        destination = roomMap[myPlayer.location][DOWN]
        movement_setup(dest)
    elif dest in ["left", "west"]:
        destination = roomMap[myPlayer.location][LEFT]
        movement_setup(dest)
    elif dest in ["right", "east"]:
        destination = roomMap[myPlayer.location][RIGHT]
        movement_setup(dest)

def movement_setup(destination):
    print("\n"+ "You have move to the" + destination)
    myPlayer.location = destination
    print_location()

def player_reveal():
    if roomMap[myPlayer.location][SOLVED] == True:
        print("no item in this room")

 # if player finds exit game over  
def game_logic():
    while myPlayer.game_over == False:
        prompt()


def setup_game():
    os.system("clear")
    Q1 = "What's your name?"
    
    for character in Q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

os.system("clear")
print("Let's start now!")
game_logic()


menu()