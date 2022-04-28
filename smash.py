#-*- coding: utf-8 -*-
from ast import match_case
from email.policy import default
import time
import os
from tkinter import ALL
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
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


correctLink = False

while correctLink == False:
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


        print(len(sets))
        for i in sets:
            if len(i["entrant1Name"].split("|")) > 1:
                p1TempName = i["entrant1Name"].split("| ")[1]
            else:
                p1TempName = i["entrant1Name"]

            if len(i["entrant2Name"].split("|")) > 1:
                p2TempName = i["entrant2Name"].split("| ")[1]
            else:
                p2TempName = i["entrant2Name"]


            if i["entrant1Score"] == -1:
                print("| ",i["fullRoundText"]," ->", setNumber,"<- ", "|", p1TempName,  "vs." , p2TempName, " | ", "No score reported")
            else:
                print("| ",i["fullRoundText"]," ->", setNumber,"<- ", "|", p1TempName,  "vs." , p2TempName, " | ", i["entrant1Score"] , "-" , i["entrant2Score"])

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
    

    
    def setSelect():
        print("\n")
        print("Select set to stream:", end = " ")
        selectedSet = int(input()) - 1
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

        else:
            print("Refreshing List...")

    def selectPorts():
        print("Player 1", "s port", "1 - 4")

        _p1Port = input()
        player1Port = _p1Port
        p1PortSelected = "port/" + _p1Port + ".png"
        shutil.copyfile(p1PortSelected, "player1/port.png")


        print("Player 2", "s port", "1 - 4")
        
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
                
        clearConsole()
        printSetInfo()
        print("1 to select match for stream")
        print("2 to select port numbers")
        print("3 to select a different tournament")
        inp = int(input())
        match inp:
            case 1:
                setSelect()
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
            


