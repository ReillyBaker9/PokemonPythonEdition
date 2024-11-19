from Classes import *
from Pokedex import *
from random import randint

def initializeGame():
    global Player
    # Player.name = input("What is your name? ")
    Player.name = "Reilly"
    Player.team = []
    Player.x = 0
    Player.y = 0

    # temporarily set team to three starter evos
    Player.team.append(Pokedex[2])
    Player.team.append(Pokedex[5])
    Player.team.append(Pokedex[8])

    for k in range(len(Player.team)):
            print(Player.team[k].name)

    # for i in range(3):
        # for listing the available options. Leaving disabled
        # print("Choose a Pokemon:")
        # for j in range(len(Pokedex)):
        #     print(str(j + 1) + ". " + Pokedex[j].name)

        # for choosing a Pokemon. Auto assigning for now
        # choice = int(input("Enter the number of the Pokemon you want: ")) - 1
        # Player.team.append(Pokedex[choice])
        # print("You chose " + Pokedex[choice].name + "!")
        # print("Your team so far: ")
        

def startBattle():
    opponent = Opponent("Gary", [Pidgey, Caterpie, Charmander])
    print("You are challenged by " + opponent.name + "!")
    print("Opponent's team: ")
    for i in range(len(opponent.team)):
        print(opponent.team[i].name)
    # global PlayerMon
    PlayerMon = Player.team[0]
    tempHP = PlayerMon.hp
    tempAtk = PlayerMon.attack
    tempDefense = PlayerMon.defense
    tempSpAtk = PlayerMon.spattack
    tempSpDef = PlayerMon.spdefense
    tempSpeed = PlayerMon.speed
    # global OpponentMon
    OpponentMon = opponent.team[0]
    oppHP = OpponentMon.hp
    oppAtk = OpponentMon.attack
    oppDefense = OpponentMon.defense
    oppSpAtk = OpponentMon.spattack
    oppSpDef = OpponentMon.spdefense
    oppSpeed = OpponentMon.speed
    print("Go! " + PlayerMon.name + "!")
    print("Opponent sent out " + OpponentMon.name + "!")
    playerTurn(PlayerMon, OpponentMon)

def playerTurn(PlayerMon, OpponentMon):
    def calcDamage(move, PlayerMon, OpponentMon):
        print(move.power)
        print(tempAtk)
        print(oppDefense)
    def checkAccuracy(move):
        check = randint(1, 100)
        if check > move.accuracy:
            print(move.name + " missed!")
            return
        else:
            calcDamage(move, PlayerMon, OpponentMon)

    def playerSwitch(PlayerMon):
        for k in range(len(Player.team)):
            print(str(k + 1) + ". " + Player.team[k].name)
        mon = int(input("Which Pokemon will you switch to? ")) - 1
        if Player.team[mon] == PlayerMon:
            print("Can't switch to the Pokemon already out!")
            return playerSwitch(PlayerMon)
        else:
            PlayerMon = Player.team[mon]
            print("Switched to " + PlayerMon.name)
            return PlayerMon
    
    def setStats(PlayerMon, OpponentMon, operation):
        return
    
    def opponentTurn(PlayerMon):
        print("Opponent made a move!")
        playerTurn(PlayerMon, OpponentMon)
        return
    
    # leave it as 0 for now
    statChange = 0
    if statChange == 1:
        setStats()
    else:
        tempHP = PlayerMon.hp
        tempAtk = PlayerMon.attack
        tempDefense = PlayerMon.defense
        tempSpAtk = PlayerMon.spattack
        tempSpDef = PlayerMon.spdefense
        tempSpeed = PlayerMon.speed
        oppHP = OpponentMon.hp
        oppAtk = OpponentMon.attack
        oppDefense = OpponentMon.defense
        oppSpAtk = OpponentMon.spattack
        oppSpDef = OpponentMon.spdefense
        oppSpeed = OpponentMon.speed
    print("What will you do?")
    print("1. Fight")
    print("2. Switch Pokemon")
    print("3. Bag")
    battleChoice = input("Choice: ")
    if battleChoice == "1":
        print("Use which move?")
        for i in range(len(PlayerMon.moves)): 
            print(str(i+1) + ". " + str(PlayerMon.moves[i].name))
        moveIndex = int(input("Select move: ")) - 1
        checkAccuracy(PlayerMon.moves[moveIndex])
        opponentTurn(PlayerMon)
    if battleChoice == "2":
        opponentTurn(playerSwitch(PlayerMon))

def main():
    print("Welcome to Pokemon!")
    initializeGame()
    startBattle()

main()