import sys
import random

playerChoose = sys.argv[1]

chooses = ["tijera", "roca", "papel"]

iaChoose = random.randint(0, 2)

print("ia choose: " + chooses[iaChoose])

playerChooseId = 0

for x in range(0,len(chooses)):
    if(chooses[x] == playerChoose):
        playerChooseId = x

print("player choose: " + playerChoose)  

#evaluar la jugada humana vs la maquina
#si playerChoose es tijera id = 0
#si playerChoose es roca id = 1
#si playerChoose es papel id = 2

# 0 > 2 == true
# 2 > 1 == true
# 1 > 0 == true

win = ""
if playerChooseId == 0 and iaChoose == 2:
    # win player
    win = "player"
if iaChoose == 0 and playerChooseId == 2:
    #win ia
    win = "ia"

if playerChooseId == 2 and iaChoose == 1:
    # win player
    win = "player"
if iaChoose == 2 and playerChooseId == 1:
    #win ia
    win = "ia"

if playerChooseId == 1 and iaChoose == 0:
    # win player
    win = "player"
if iaChoose == 1 and playerChooseId == 0:
    #win ia
    win = "ia"
if iaChoose == playerChooseId:
    #win empate
    win = "empate"

print("the winner of the match is: {}".format(win))