#-*- coding: utf-8 -*-
import pyfiglet
result = pyfiglet.figlet_format("  Smash Scrape", font = "slant")
from ast import match_case
from email.policy import default
import time
import os
from tkinter import ALL
from turtle import end_fill

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def move (x, y):
    print("\033[%d;%dH" % (x, y), end="")

from PIL import Image
import sys
import requests
import shutil
import pysmashgg
key = "338febc91f4322942391fac3ef99f455"
smash = pysmashgg.SmashGG(key)
port1 = Image.open("port/1.png")
port2 = Image.open("port/2.png")
port3 = Image.open("port/3.png")
port4 = Image.open("port/4.png")

player1Port = 0
player2Port = 0

selectedSet = 32132

_activeSets = 0
setsLeft = True


tourney = ""
#print(str("https://smash.gg/admin/tournament/test-tournament-869/event/melee-singles/set/46746437".split("/", 5)[0]))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
print(result)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")

_input = ""
while(_input != "y" and _input != "n"):
    print("Load previous tournament",'"', end="")
    with open("currentTourneyName.txt" , "r") as f:
        print(f.readline(), end="")
    print('" ?',"(y/n)")
    _input = input()
    if _input == "n":
        correctLink = False
        while correctLink == False:
            print("smash.gg link: ", end="")

            _inp = input()

            if str(_inp.split("/")[3]) == "admin":
                tourney = str(_inp.split("/")[5])
                correctLink = True
                with open("currentTourneyName.txt", "w") as f:
                    f.write(tourney)
            elif str(_inp.split("/")[3]) == "tournament":
                tourney = str(_inp.split("/")[4])
                correctLink = True
                with open("currentTourneyName.txt", "w") as f:
                    f.write(tourney)
            elif str(_inp.split("/")[0] != "https:"):
                print("Paste full link")
            
    elif _input == "y":
        with open("currentTourneyName.txt", "r") as f:
            if f.readline() != "":
                with open("currentTourneyName.txt", "r") as f:
                    tourney = f.readline()
                    correctLink = True
            else:
                clearConsole()
                print("No saved tournament")
                _input = ""
    else:
        clearConsole()
 

        
print(tourney)





        


# for i in sets:
#     print(i["entrant1Score"], end=" ")
#     print(i["entrant2Score"], end=" | ")
#     print(i["completed"], end=" | ")
#     print(i["winnerName"], end=" | ")
#     print()
    

# p1Port = Image.open("player1/port.png")
# p2Port = Image.open("player2/port.png")

print("Loading bracket info...")


    

def printSetInfo():

        sets = smash.tournament_show_sets(tourney, 'melee-singles', 1) + smash.tournament_show_sets(tourney, 'melee-singles', 2) + smash.tournament_show_sets(tourney, 'melee-singles', 3) 

        # for i in sets1:
        #     print(i["entrant2Name"]," - ", i["entrant1Name"] , "\n")
        setNumber = 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")

        print("",tournament["name"] ,"", "\n")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" , "\n")


        for i in sets:
            setID = i["id"]
            matchText = i["fullRoundText"]

        print("___________________________", "\n")

        print("Current StreamLabs Info")

        print("___________________________" , "\n")

        with open('matchTitle.txt') as f:
            print("|", f.readline(), "\n\n")

        with open('player1/name.txt') as f:
            print("|  ",f.readline(), "vs.", end=" ")

        with open('player2/name.txt') as f:
            print(f.readline())

        with open('player1/score.txt') as f:
            print("|  ", f.readline(), "-", end=" ")

        with open('player2/score.txt') as f:
            print(f.readline(), "\n")
        print("___________________________", "\n")

        print("Sets @ smash.gg")

        print("___________________________" , "\n")

        increase = 0

        for i in sets:
            increase += 1
            if len(i["entrant1Name"].split("|")) > 1:
                p1TempName = i["entrant1Name"].split("| ")[1]
            else:
                p1TempName = i["entrant1Name"]

            if len(i["entrant2Name"].split("|")) > 1:
                p2TempName = i["entrant2Name"].split("| ")[1]
            else:
                p2TempName = i["entrant2Name"]


            if i["entrant1Score"] == -1 and i["entrant2Score"] == -1:
                move(40, 0)
                print(" ->", setNumber,"<- ", end="")
                move(40, 10)
                print("|", p1TempName, end="")
                move(40, 25)
                print("  vs." , p2TempName, end="")
                move(40, 50)
                print(" | ", i["fullRoundText"], end="")
                move(40, 80)
                print(" | ", i["fullRoundText"] ," | ", "No score reported")
            elif i["entrant1Score"] == -1 and i["entrant2Score"] != -1:
                move(40, 0)
                print(" ->", setNumber,"<- ", end="")
                move(40, 10)
                print("|", p2TempName, end="")
                move(40, 25)
                print("  vs." , i["entrant1Name"], "(DQ)", end="")
                move(40, 50)
                print(" | ", i["fullRoundText"], end="")
                move(40, 80)
                print(" | ", "DQ", i["entrant1Name"])
            elif i["entrant2Score"] == -1 and i["entrant1Score"] != -1:
                move(40, 0)
                print(" ->", setNumber,"<- ", end="")
                move(40, 10)
                print("|", p1TempName, end="")
                move(40, 25)
                print("  vs." , i["entrant2Name"], "(DQ)", end="")
                move(40, 50)
                print(" | ", i["fullRoundText"], end="")
                move(40, 80)
                print(" | ", "DQ", "(", i["entrant2Name"] , ")")
            else:
                move(40, 0)
                print(" ->", setNumber,"<- ", end="")
                move(40, 10)
                print("|", p1TempName, end="")
                move(40, 25)
                print("  vs." , p2TempName, end="")
                move(40, 50)
                print(" | ", i["fullRoundText"], end="")
                move(40, 80)
                print(" | ", i["entrant1Score"] , "-" , i["entrant2Score"])
            setNumber += 1
        
        print()

        


sets = smash.tournament_show_sets(tourney, 'melee-singles', 1) + smash.tournament_show_sets(tourney, 'melee-singles', 2) + smash.tournament_show_sets(tourney, 'melee-singles', 3) 

for i in sets:
    if not i["entrant1Score"] == -1:
        _activeSets += 1

while _activeSets > 0:
    tournament = smash.tournament_show(tourney)

    with open('tourneyName.txt', 'w', encoding='utf-8') as f:
                f.write(tournament["name"])

    sets = smash.tournament_show_sets(tourney, 'melee-singles', 1) + smash.tournament_show_sets(tourney, 'melee-singles', 2) + smash.tournament_show_sets(tourney, 'melee-singles', 3)

    # print(sets[0], "\n")

    setID = len(sets)
    
    class setSelectClass():
        streamSet = 0
        def setSelect(selectedSet):
            streamSet = selectedSet
            if selectedSet >= 0 and selectedSet < len(sets):
                print("\n\n")
                clearConsole()
                print(sets[selectedSet]["entrant1Name"],"( Port", player1Port,")", "vs.", sets[selectedSet]["entrant2Name"],"( Port", player1Port,")", "<-----")
                print("Updating text files...")
                with open('player1/name.txt', 'w') as f:
                    f.write(sets[selectedSet]["entrant1Name"])
                with open('player2/name.txt', 'w') as f:
                    f.write(sets[selectedSet]["entrant2Name"])
                with open('matchTitle.txt', 'w') as f:
                    f.write(sets[selectedSet]["fullRoundText"])

                print("SCORE WRITING CODE")
                with open('player1/score.txt', 'w') as f:
                    f.write(str(sets[selectedSet]["entrant1Score"]))
                with open('player2/score.txt', 'w') as f:
                    f.write(str(sets[selectedSet]["entrant2Score"]))

    def selectPorts():
        print("Port [ 1 - 4 ]")
        print("Player 1: ", end=" ")
        _p1Port = input()
        player1Port = _p1Port
        p1PortSelected = "port/" + _p1Port + ".png"
        shutil.copyfile(p1PortSelected, "player1/port.png")

        print("Port [ 1 - 4 ]")
        print("Player 2: ", end=" ")
        _p2Port = input()
        player2Port = _p2Port
        p2PortSelected = "port/" + _p2Port + ".png" 
        shutil.copyfile(p2PortSelected, "player2/port.png")
        
        

        # with open('player1/score.txt', 'w') as f:
        #     f.write(str(sets[int(selectedSet)- 1]["entrant1Score"]))


    inp = 0


    while inp < 1 or inp > 3:
        while correctLink == False:
            clearConsole()
            print("smash.gg link: ", end="")

            _inp = input()

            if str(_inp.split("/")[3]) == "admin":
                tourney = str(_inp.split("/")[5])
                correctLink = True
            elif str(_inp.split("/")[3]) == "tournament":
                tourney = str(_inp.split("/")[4])
                correctLink = True
            elif str(_inp.split("/")[0] != "https:"):
                print("Paste full link")
            with open("currentTourneyName.txt", "w") as f:
                f.write(tourney)
                
        clearConsole()
        printSetInfo()
        print("     0: Update score/info/list")
        print("     1: Choose set for stream")
        print("     2: Choose port numbers")
        print("     3: Load a different tournament")
        inp = int(input())
        match inp:
            case 0:
                setSelectClass.setSelect(setSelectClass.streamSet)
            case 1:
                print("\n")
                print("Select set to stream:", end = " ")
                setSelectClass.setSelect(int(input()) - 1)
                inp ="0"
                break
            case 2:
                selectPorts()
                inp = "0"
                break
            case 3:
                correctLink = False
                inp = "0"
                break
            
                
else:
    print("\n")
    print("poo")
    # print(activeSets, "active sets")
    # print(friendlySetups, "setups for friendlies")
    print("\n")
    # print(p1Tag)
    # print(p2Tag)
            


