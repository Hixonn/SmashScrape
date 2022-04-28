#-*- coding: utf-8 -*-
import time
import os
from PIL import Image
import sys
import requests
import shutil
import pysmashgg
key = "338febc91f4322942391fac3ef99f455"
smash = pysmashgg.SmashGG(key)

def smashGGLink():
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

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def selectPorts():
    sets = smash.tournament_show_sets(tourney, 'melee-singles', 1)
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

def setSelect():
    sets = smash.tournament_show_sets(tourney, 'melee-singles', 1)
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

def printSetInfo():
    sets = smash.tournament_show_sets(tourney, 'melee-singles', 1)

    for i in sets:
        print("Game completed:", i["completed"] , "\n")

    selectedSet = 0
    setNumber = 1
    activeSets = 0
    
    print("~",tournament["name"] ,"~", "\n")

    for i in range(len(sets)):
        setID = sets[i]["id"]
        matchText = sets[i]["fullRoundText"]

    if totalSetups - activeSets < 0:
        friendlySetups = 0
    else:
        friendlySetups = totalSetups - activeSets

    with open('friendlySetups.txt', 'w') as f:
        f.write(str(friendlySetups))
    print()
    print("___________________________", "\n")

    print("Sets @ smash.gg")

    print("___________________________" , "\n")


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
            print(" ->", setNumber,"<- ", "|", p1TempName,  "vs." , p2TempName, " | ", "No score reported")
        else:
            print(" ->", setNumber,"<- ", "|", p1TempName,  "vs." , p2TempName, " | ", i["entrant1Score"] , "-" , i["entrant2Score"])

        setNumber += 1
    
    print()

