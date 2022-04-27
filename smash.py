#-*- coding: utf-8 -*-
from PIL import Image
import sys
import requests
import shutil
import pysmashgg

sets = ""

def updateSets():
    sets = smash.tournament_show_sets(tourney, 'melee-singles', 1)
    return len(sets)

port1 = Image.open("port/1.png")
port2 = Image.open("port/2.png")
port3 = Image.open("port/3.png")
port4 = Image.open("port/4.png")

# p1Port = Image.open("player1/port.png")
# p2Port = Image.open("player2/port.png")

key = "338febc91f4322942391fac3ef99f455"
smash = pysmashgg.SmashGG(key)

_activeSets = 0
setsLeft = True

print("Paste smash.gg link: ", end="")
tourney = str(input().split("/", 5)[4])
print(tourney)

print("Type the number of available melee setups: ", end="")
totalSetups = int(input())
print("Loading bracket info...")
print("\n\n")

updateSets()

for i in range(updateSets()):
    if not sets[i]["completed"]:
        _activeSets += 1

while _activeSets > 0:
    selectedSet = 0
    activeSets = 0
    setNumber = 1

    with open('tourneyName.txt', 'w', encoding='utf-8') as f:
                f.write(tournament["name"])

    updateSets()

    # print(sets[0], "\n")

    setID = len(sets)

    for i in range(len(sets)):
        setID = sets[i]["id"]
        matchText = sets[i]["fullRoundText"]

    for i in sets:
        if not i["completed"]:
            if len(i["entrant1Name"].split("|")) > 1:
                p1TempName = i["entrant1Name"].split("| ")[1]
            else:
                p1TempName = i["entrant1Name"]

            if len(i["entrant2Name"].split("|")) > 1:
                p2TempName = i["entrant2Name"].split("| ")[1]
            else:
                p2TempName = i["entrant2Name"]


            print(setNumber, "-", p1TempName,  "vs." , p2TempName)
            setNumber += 1
            activeSets += 1

    if totalSetups - activeSets < 0:
        friendlySetups = 0
    else:
        friendlySetups = totalSetups - activeSets

    def printSetInfo():
        print("\n")
        print("Select set number (0 to update list/info/score):", end = " ")
        selectedSet = input()
        if not int(selectedSet) < 1 and not int(selectedSet) > len(sets):
            print("\n\n")
            print(sets[int(selectedSet) - 1]["entrant1Name"], "vs.", sets[int(selectedSet) - 1]["entrant2Name"], "<-----")
            print("Updating text files...")
            with open('player1/name.txt', 'w') as f:
                f.write(sets[int(selectedSet) - 1]["entrant1Name"])
            with open('player2/name.txt', 'w') as f:
                f.write(sets[int(selectedSet) - 1]["entrant2Name"])
            with open('matchTitle.txt', 'w') as f:
                f.write(sets[int(selectedSet)- 1]["fullRoundText"])
            with open('friendlySetups.txt', 'w') as f:
                f.write(str(friendlySetups))

            if sets[int(selectedSet)- 1]["entrant1Score"] >= 0:
                with open('player1/score.txt', 'w') as f:
                    f.write(str(sets[int(selectedSet)- 1]["entrant1Score"]))
                with open('player2/score.txt', 'w') as f:
                    f.write(str(sets[int(selectedSet)- 1]["entrant2Score"]))
            else:
                with open('player1/score.txt', 'w') as f:
                    f.write("0")
                with open('player2/score.txt', 'w') as f:
                    f.write("0")
        else:
            print("Refreshing List...")

    def selectPorts():
        print("\n")
        print("Select Player 1's port", "1 or 2 or 3 or 4")

        _p1Port = input()
        p1PortSelected = "port/" + _p1Port + ".png"
        shutil.copyfile(p1PortSelected, "player1/port.png")


        print("Select Player 2's port", "1 or 2 or 3 or 4")
        
        _p2Port = input()
        p2PortSelected = "port/" + _p2Port + ".png" 
        shutil.copyfile(p2PortSelected, "player2/port.png")
        
        

        # with open('player1/score.txt', 'w') as f:
        #     f.write(str(sets[int(selectedSet)- 1]["entrant1Score"]))
else:
    print("Tournament over. No active sets.")
        
        


    printSetInfo()
    selectPorts()






    print("\n")
    print(activeSets, "active sets")
    print(friendlySetups, "setups for friendlies")
    print("\n")
    # print(p1Tag)
    # print(p2Tag)
            


